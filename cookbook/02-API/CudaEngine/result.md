[07/19/2022-17:12:51] [TRT] [E] 3: Get bytes per component failed, getBindingVectorizedDim() result shall not equal -1.
main.py:56: DeprecationWarning: Use network created with NetworkDefinitionCreationFlag::EXPLICIT_BATCH flag instead.
  print("engine.max_batch_size = %d" % engine.max_batch_size)
engine.device_memory_size = 0
engine.engine_capability = 0
engine.has_implicit_batch_dimension = False
engine.max_batch_size = 1
engine.name = Unnamed Network 0
engine.num_bindings = 2
engine.num_layers = 1
engine.num_optimization_profiles = 1
engine.refittable = False
engine.tactic_sources = 0
engine.__len__() = 2
engine.__sizeof__() = 56
engine.__str__() = <tensorrt.tensorrt.ICudaEngine object at 0x7fde685ea970>


Method related to binding:
Binding:                                                                                    0,                                                         1
get_binding_name:                                                                     inputT0,                      (Unnamed Layer* 0) [Identity]_output
get_binding_shape:                                                              (-1, 4, 8, 8),                                             (-1, 4, 8, 8)
get_binding_dtype:                                                             DataType.FLOAT,                                             DataType.INT8
get_binding_format:                                                       TensorFormat.LINEAR,                                         TensorFormat.CHW4
get_binding_format_desc:                               Row major linear FP32 format (kLINEAR),Four wide channel vectorized row major INT8 format (kCHW4)
get_binding_bytes_per_component:                                                            0,                                                         1
get_binding_components_per_element:                                                        -1,                                                         4
get_binding_vectorized_dim:                                                                -1,                                                         1

binding_is_input:                                                                        True,                                                     False
is_execution_binding:                                                                    True,                                                      True
is_shape_binding:                                                                       False,                                                     False
get_profile_shape:                                 [(1, 4, 8, 8), (1, 4, 8, 8), (2, 4, 8, 8)],                                                          
__getitem__(int):                                                                     inputT0,                      (Unnamed Layer* 0) [Identity]_output
__getitem__(str):                                                                           0,                                                         1
get_binding_index:                                                                          0,                                                         1
Input 0: (1, 4, 8, 8) 
 [[[[  0.5   1.    1.5   2.    2.5   3.    3.5   4. ]
   [  4.5   5.    5.5   6.    6.5   7.    7.5   8. ]
   [  8.5   9.    9.5  10.   10.5  11.   11.5  12. ]
   [ 12.5  13.   13.5  14.   14.5  15.   15.5  16. ]
   [ 16.5  17.   17.5  18.   18.5  19.   19.5  20. ]
   [ 20.5  21.   21.5  22.   22.5  23.   23.5  24. ]
   [ 24.5  25.   25.5  26.   26.5  27.   27.5  28. ]
   [ 28.5  29.   29.5  30.   30.5  31.   31.5  32. ]]

  [[ 32.5  33.   33.5  34.   34.5  35.   35.5  36. ]
   [ 36.5  37.   37.5  38.   38.5  39.   39.5  40. ]
   [ 40.5  41.   41.5  42.   42.5  43.   43.5  44. ]
   [ 44.5  45.   45.5  46.   46.5  47.   47.5  48. ]
   [ 48.5  49.   49.5  50.   50.5  51.   51.5  52. ]
   [ 52.5  53.   53.5  54.   54.5  55.   55.5  56. ]
   [ 56.5  57.   57.5  58.   58.5  59.   59.5  60. ]
   [ 60.5  61.   61.5  62.   62.5  63.   63.5  64. ]]

  [[ 64.5  65.   65.5  66.   66.5  67.   67.5  68. ]
   [ 68.5  69.   69.5  70.   70.5  71.   71.5  72. ]
   [ 72.5  73.   73.5  74.   74.5  75.   75.5  76. ]
   [ 76.5  77.   77.5  78.   78.5  79.   79.5  80. ]
   [ 80.5  81.   81.5  82.   82.5  83.   83.5  84. ]
   [ 84.5  85.   85.5  86.   86.5  87.   87.5  88. ]
   [ 88.5  89.   89.5  90.   90.5  91.   91.5  92. ]
   [ 92.5  93.   93.5  94.   94.5  95.   95.5  96. ]]

  [[ 96.5  97.   97.5  98.   98.5  99.   99.5 100. ]
   [100.5 101.  101.5 102.  102.5 103.  103.5 104. ]
   [104.5 105.  105.5 106.  106.5 107.  107.5 108. ]
   [108.5 109.  109.5 110.  110.5 111.  111.5 112. ]
   [112.5 113.  113.5 114.  114.5 115.  115.5 116. ]
   [116.5 117.  117.5 118.  118.5 119.  119.5 120. ]
   [120.5 121.  121.5 122.  122.5 123.  123.5 124. ]
   [124.5 125.  125.5 126.  126.5 127.  127.5 128. ]]]]
Output 0: (1, 4, 8, 8) 
 [[[[  0  32  64  96   1  33  64  96]
   [  1  33  65  97   2  34  65  97]
   [  2  34  66  98   3  35  66  98]
   [  3  35  67  99   4  36  67  99]
   [  4  36  68 100   5  37  68 100]
   [  5  37  69 101   6  38  69 101]
   [  6  38  70 102   7  39  70 102]
   [  7  39  71 103   8  40  71 103]]

  [[  8  40  72 104   9  41  72 104]
   [  9  41  73 105  10  42  73 105]
   [ 10  42  74 106  11  43  74 106]
   [ 11  43  75 107  12  44  75 107]
   [ 12  44  76 108  13  45  76 108]
   [ 13  45  77 109  14  46  77 109]
   [ 14  46  78 110  15  47  78 110]
   [ 15  47  79 111  16  48  79 111]]

  [[ 16  48  80 112  17  49  80 112]
   [ 17  49  81 113  18  50  81 113]
   [ 18  50  82 114  19  51  82 114]
   [ 19  51  83 115  20  52  83 115]
   [ 20  52  84 116  21  53  84 116]
   [ 21  53  85 117  22  54  85 117]
   [ 22  54  86 118  23  55  86 118]
   [ 23  55  87 119  24  56  87 119]]

  [[ 24  56  88 120  25  57  88 120]
   [ 25  57  89 121  26  58  89 121]
   [ 26  58  90 122  27  59  90 122]
   [ 27  59  91 123  28  60  91 123]
   [ 28  60  92 124  29  61  92 124]
   [ 29  61  93 125  30  62  93 125]
   [ 30  62  94 126  31  63  94 126]
   [ 31  63  95 127  32  64  95 127]]]]