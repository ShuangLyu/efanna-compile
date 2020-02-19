import ctypes
lib = ctypes.cdll.LoadLibrary("./libefanna2e.so")
string1 = "./sift_base.fvecs"
string2 = "./saved_data2020"
b_string1 = string1.encode("utf-8")
b_string2 = string2.encode("utf-8")
s1 = ctypes.c_char_p(b_string1)
s2 = ctypes.c_char_p(b_string2)
lib.foo(s1,s2,10,20,30,40,50)
