# kernelpy
A simple library for generating convolution matrices for GLSL in Python. 

# Examples

<h3>Code: </h3>

    from random import randrange
    import kernelpy
    
    def example_f(kernel_index, function_index) :
    	return randrange(-5, 5)/5
    
    myBuilder = kernelpy.builder.KernelBuilder("myKernel", "vec2", 3, 16, functions=(example_f, example_f))
    myBuilder.run()
    print(myBuilder.array)
    print(myBuilder.to_str()) 
<h3>Output: </h3>

    
        > test_kern.py
    Array: [[-1.0, -1.0], [0.6, 0.6], [-0.4, -0.2], [-1.0, -0.4], [0.6, -0.8], [0.4, -0.6], [-1.0, 0.2], [-0.8, 0.4], [0.0, 0.6], [-0.8, -0.2], [-0.2, 0.2], [0.8, -0.4], [-1.0, 0.4], [-0.4, -1.0], [0.8, 0.4], [-1.0, 0.6]]
    String: const vec2[16] myKernel = vec2[](vec2(-1.000, -1.000),vec2(0.600, 0.600),vec2(-0.400, -0.200),vec2(-1.000, -0.400),
    vec2(0.600, -0.800),vec2(0.400, -0.600),vec2(-1.000, 0.200),vec2(-0.800, 0.400),
    vec2(0.000, 0.600),vec2(-0.800, -0.200),vec2(-0.200, 0.200),vec2(0.800, -0.400),
    vec2(-1.000, 0.400),vec2(-0.400, -1.000),vec2(0.800, 0.400),vec2(-1.000, 0.600));

# License
Copyright (c) 2024 Velvet C. Licensed under the [MIT License](https://github.com/VelvetCauliflower/kernelpy/blob/main/LICENSE).
