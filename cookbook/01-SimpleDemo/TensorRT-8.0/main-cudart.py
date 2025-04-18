# SPDX-FileCopyrightText: Copyright (c) 1993-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import numpy as np
import tensorrt as trt
from cuda import cudart  # using CUDA Runtime API

# yapf:disable

trt_file = "model.trt"
data = np.arange(3 * 4 * 5, dtype=np.float32).reshape(3, 4, 5)                  # input data for inference

def run():
    logger = trt.Logger(trt.Logger.ERROR)                                       # Logger, available level: VERBOSE, INFO, WARNING, ERROR, INTERNAL_ERROR
    if os.path.isfile(trt_file):                                                # read .trt file if exists
        with open(trt_file, "rb") as f:
            engineString = f.read()
        if engineString == None:
            print("Fail getting serialized engine")
            return
        print("Succeed getting serialized engine")
    else:                                                                       # no .trt file, build engine from scratch
        builder = trt.Builder(logger)                                           # meta data of the network
        network = builder.create_network(1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH))
        profile = builder.create_optimization_profile()
        config = builder.create_builder_config()
        config.max_workspace_size = 1 << 30                                     # set workspace for TensorRT

        inputTensor = network.add_input("inputT0", trt.float32, [-1, -1, -1])   # set input tensor of the network
        profile.set_shape(inputTensor.name, [1, 1, 1], [3, 4, 5], [6, 8, 10])   # set dynamic shape range of the input tensor
        config.add_optimization_profile(profile)

        identityLayer = network.add_identity(inputTensor)                       # add a layer of identity operator
        network.mark_output(identityLayer.get_output(0))                        # set output tensor of the network

        engineString = builder.build_serialized_network(network, config)        # create a serialized network from the network
        if engineString == None:
            print("Fail building serialized engine")
            return
        print("Succeed building serialized engine")
        with open(trt_file, "wb") as f:                                          # save the serialized network as binaray file
            f.write(engineString)
            print("Succeed saving .trt file")

    engine = trt.Runtime(logger).deserialize_cuda_engine(engineString)          # create inference engine using Runtime
    if engine == None:
        print("Fail building engine")
        return
    print("Succeed building engine")

    context = engine.create_execution_context()                                 # create CUDA context (similar to a process on GPU)
    context.set_binding_shape(0, [3, 4, 5])                                     # bind actual shape of the input tensor in Dynamic Shape mode
    nInput = np.sum([engine.binding_is_input(i) for i in range(engine.num_bindings)])  # get information of the TensorRT engine
    nOutput = engine.num_bindings - nInput
    for i in range(nInput):
        print("Bind[%2d]:i[%2d]->" % (i, i), engine.get_binding_dtype(i), engine.get_binding_shape(i), context.get_binding_shape(i), engine.get_binding_name(i))
    for i in range(nInput, nInput + nOutput):
        print("Bind[%2d]:o[%2d]->" % (i, i - nInput), engine.get_binding_dtype(i), engine.get_binding_shape(i), context.get_binding_shape(i), engine.get_binding_name(i))

    bufferH = []
    bufferH.append(np.ascontiguousarray(data))
    for i in range(nInput, nInput + nOutput):
        bufferH.append(np.empty(context.get_binding_shape(i), dtype=trt.nptype(engine.get_binding_dtype(i))))
    bufferD = []
    for i in range(nInput + nOutput):
        bufferD.append(cudart.cudaMalloc(bufferH[i].nbytes)[1])

    for i in range(nInput):                                                     # copy the data from host to device
        cudart.cudaMemcpy(bufferD[i], bufferH[i].ctypes.data, bufferH[i].nbytes, cudart.cudaMemcpyKind.cudaMemcpyHostToDevice)

    context.execute_v2(bufferD)                                                 # do inference computation

    for i in range(nInput, nInput + nOutput):                                   # copy the result from device to host
        cudart.cudaMemcpy(bufferH[i].ctypes.data, bufferD[i], bufferH[i].nbytes, cudart.cudaMemcpyKind.cudaMemcpyDeviceToHost)

    for i in range(nInput + nOutput):
        print(engine.get_binding_name(i))
        print(bufferH[i])

    for b in bufferD:                                                           # free the buffer on device
        cudart.cudaFree(b)

if __name__ == "__main__":
    os.system("rm -rf *.trt")
    run()                                                                       # create TensorRT engine and do inference
    run()                                                                       # load TensorRT engine from file and do inference
