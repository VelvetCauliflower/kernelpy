# A simple library for generating convolution matrices for GLSL and HLSL.

from math import floor

def _builder_dummy_function(kernel_index, function_index) :
	return 0


class KernelBuilder :
	def __init__(self, name = "myKernel", data_type = "vec2", float_precision = 3, length = 16, functions = (_builder_dummy_function,  _builder_dummy_function)) :
		self.set_float_precision(float_precision)
		self.set_function(functions)
		self.set_data_type(data_type)
		self.set_length(length)
		self.set_name(name)
		self.array = []
		
	def set_name(self, name) :
		self.name = name
		
	def set_length(self, length) :
		self.length = length
		
	def set_float_precision(self, float_precision) :
		if not type(float_precision) is int :
			raise Exception("Argument must be an integer to set floating point precision.")
		self.float_precision = "{:1." + str(float_precision) + "f}"
		
	def set_function(self,  functions) :
		self.functions = functions
		
	def set_data_type(self, data_type) :
		self.data_type = data_type
		
	def run(self) :
		self.array.clear()
		for kernel_index in range(self.length) :
			scale = 1
			data = []
			function_index = -1
			for f in self.functions :
				function_index+=1
				result = f(kernel_index, function_index)
				if result != None :
					data.append(result)
			if len(data) > 0 :
				self.array.append(data)
		
	def to_str(self, new_line=4) :
		if len(self.array) == 0 :
			raise Exception("Kernel has not been loaded. Call Kernel.run() before calling Kernel.to_str()")
		i = -1
		full_str = "const " + self.data_type+ "["+ str(self.length) +"] "+ self.name + " = " + self.data_type+ "[]("
		for item in self.array:
			i+=1
			full_str += self.data_type+"(" 
			for data in item :	
				full_str +=  self.float_precision.format(data) + ", "
			full_str = full_str[0:len(full_str)-2]
			full_str += "),"
			if (i+1)/new_line == floor((i+1)/new_line) and i != self.length :
				full_str += "\n"
		full_str = full_str[0:len(full_str)-2] + ");"
		return full_str
		
		
def convolution_kernel_string(new_line, name, data_type, float_precision, length, functions) :
	temp_kernel = Kernel(name, data_type, float_precision, length, functions)
	temp_kernel.run()
	return temp_kernel.to_str(new_line)
	
