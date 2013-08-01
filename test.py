"""
/**
 * (C) 2010-2011 Alibaba Group Holding Limited.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License 
 * version 2 as published by the Free Software Foundation. 
 * 
 */
 
"""

class MyClass:
    __a=10;# private
    _b=100;#public
    def __init__(self,name='zemi'):
        self.name=name
        print("__init__",self);
    def __del__(self):
        print("__del__");
    def go(self):
        print("go");
    def run(self):
        pass	# 空操作语句（不做任何操作）

class SubClass(MyClass):
 def run(self,val=10):
     print("running");
    

def testFor(step=10):
 for i in range(0,step):
    print(i)

def testArray():
    arr=[1,2,3,4];
    jsonArr={'a':100,'b':'3213'};
    arr2 = [i for i in range(10)];
    print("the arr value is ",arr);
    print("the arr[0] value is ",arr[0]);
    print("the json value is a=%d ,b=%s" %(jsonArr["a"],jsonArr["b"]))
    print("jsonArr.keys,jsonArr.values:",jsonArr.keys,jsonArr.values);                                                          
    print("the arr2 value is",arr2)
    for key in jsonArr:
     print("key=%s ,jsonArr[key]=%s,jsonArr.get(key)=%s" %(key,jsonArr[key],jsonArr.get(key)));
    print("arr[1:3]=%s" %(arr[1:3]));

def  testClass():
    c=MyClass('ayf');
    print(c.name,c._b);
    sub=SubClass();
    print("**sub class is SubClass,parent Class Myclass")
    print(sub.run());
    print(sub.go());
    #print(object.__getattr__(c,name));


def testPublicAttr():
    print("__doc__:",__doc__);
    print("__name__:",__name__);
    
if(__name__=="__main__"):
    print("Welcome Use Python with Zemi")
    print("=========testFor============");
    testFor();
    print("=========testArray===========");
    testArray();
    print("=========testClass============");
    testClass();
    print("=========testPublicAttr========");
    testPublicAttr();


    input("Press enter to exit")
