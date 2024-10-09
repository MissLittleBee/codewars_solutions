"""Kata - Training JS #3:  Basic data types--String

completed at: 2024-10-08 17:43:26
by: Barbora Hůlová

In javascript, String is one of basic data types. Use ```""``` or ```''``` to declare a string variable. It can be letters:```a,b,c,A,B,C```, numbers: ```123...```, Various symbol:```@#$%^&*``` , Control symbol:```\n,\t``` etc..
    
String can use operators ```+```, Connect two or more strings together.

## Task

misson 1:
I've create three function, and defined some global variables, please select some variables that can make up the name of the function, and return them(Please note the uppercase and lowercase letters are different).

When you have finished the work, click "Run Tests" to see if your code is working properly.

misson 2:
After misson 1 finished. you should click "Attempt" to see my three questions, and write the answer in function ```answer1, answer2,answer3```

If everything is right, click "Submit" again to submit your code pass this kata.
    
## [Series](http://github.com/myjinxin2015/Katas-list-of-Training-JS-series)

( ↑↑↑ Click the link above can get my newest kata list, Please add it to your favorites)

 - [#1: create your first JS function helloWorld](http://www.codewars.com/kata/571ec274b1c8d4a61c0000c8)
 - [#2: Basic data types--Number](http://www.codewars.com/kata/571edd157e8954bab500032d)
 - [#3:  Basic data types--String](http://www.codewars.com/kata/571edea4b625edcb51000d8e)
 - [#4:  Basic data types--Array](http://www.codewars.com/kata/571effabb625ed9b0600107a)
 - [#5:  Basic data types--Object](http://www.codewars.com/kata/571f1eb77e8954a812000837)
 - [#6:  Basic data types--Boolean and conditional statements if..else](http://www.codewars.com/kata/571f832f07363d295d001ba8)
 - [#7:  if..else and ternary operator](http://www.codewars.com/kata/57202aefe8d6c514300001fd)
 - [#8: Conditional statement--switch](http://www.codewars.com/kata/572059afc2f4612825000d8a)
 - [#9: loop statement --while and do..while](http://www.codewars.com/kata/57216d4bcdd71175d6000560)
 - [#10: loop statement --for](http://www.codewars.com/kata/5721a78c283129e416000999)
 - [#11: loop statement --break,continue](http://www.codewars.com/kata/5721c189cdd71194c1000b9b)
 - [#12: loop statement --for..in and for..of](http://www.codewars.com/kata/5722b3f0bd5583cf44001000)
 - [#13: Number object and  its properties](http://www.codewars.com/kata/5722fd3ab7162a3a4500031f)
 - [#14: Methods of Number object--toString() and toLocaleString()](http://www.codewars.com/kata/57238ceaef9008adc7000603)
 - [#15: Methods of Number object--toFixed(), toExponential() and toPrecision()](http://www.codewars.com/kata/57256064856584bc47000611)
 - [#16: Methods of String object--slice(), substring() and substr()](http://www.codewars.com/kata/57274562c8dcebe77e001012)
 - [#17: Methods of String object--indexOf(), lastIndexOf() and search()](http://www.codewars.com/kata/57277a31e5e51450a4000010)
 - [#18: Methods of String object--concat() split() and its good friend join()](http://www.codewars.com/kata/57280481e8118511f7000ffa)
 - [#19: Methods of String object--toUpperCase() toLowerCase() and replace()](http://www.codewars.com/kata/5728203b7fc662a4c4000ef3)
 - [#20: Methods of String object--charAt() charCodeAt() and fromCharCode()](http://www.codewars.com/kata/57284d23e81185ae6200162a)
 - [#21: Methods of String object--trim() and the string template](http://www.codewars.com/kata/5729b103dd8bac11a900119e)
 - [#22: Unlock new skills--Arrow function,spread operator and deconstruction](http://www.codewars.com/kata/572ab0cfa3af384df7000ff8)
 - [#23: methods of arrayObject---push(), pop(), shift() and unshift()](http://www.codewars.com/kata/572af273a3af3836660014a1)
 - [#24: methods of arrayObject---splice() and slice()](http://www.codewars.com/kata/572cb264362806af46000793)
 - [#25: methods of arrayObject---reverse() and sort()](http://www.codewars.com/kata/572df796914b5ba27c000c90)
 - [#26: methods of arrayObject---map()](http://www.codewars.com/kata/572fdeb4380bb703fc00002c)
 - [#27: methods of arrayObject---filter()](http://www.codewars.com/kata/573023c81add650b84000429)
 - [#28: methods of arrayObject---every() and some()](http://www.codewars.com/kata/57308546bd9f0987c2000d07)
 - [#29: methods of arrayObject---concat() and join()](http://www.codewars.com/kata/5731861d05d14d6f50000626)
 - [#30: methods of arrayObject---reduce() and reduceRight()](http://www.codewars.com/kata/573156709a231dcec9000ee8)
 - [#31: methods of arrayObject---isArray() indexOf() and toString()](http://www.codewars.com/kata/5732b0351eb838d03300101d)
 - [#32: methods of Math---round() ceil() and floor()](http://www.codewars.com/kata/5732d3c9791aafb0e4001236)
 - [#33: methods of Math---max() min() and abs()](http://www.codewars.com/kata/5733d6c2d780e20173000baa)
 - [#34: methods of Math---pow() sqrt() and cbrt()](http://www.codewars.com/kata/5733f948d780e27df6000e33)
 - [#35: methods of Math---log() and its family](http://www.codewars.com/kata/57353de879ccaeb9f8000564)
 - [#36: methods of Math---kata author's lover:random()](http://www.codewars.com/kata/5735956413c2054a680009ec)
 - [#37: Unlock new weapon---RegExp Object](http://www.codewars.com/kata/5735e39313c205fe39001173)
 - [#38: Regular Expression--"^","$", "." and test()](http://www.codewars.com/kata/573975d3ac3eec695b0013e0)
 - [#39: Regular Expression--"?", "*", "+" and "{}"](http://www.codewars.com/kata/573bca07dffc1aa693000139)
 - [#40: Regular Expression--"|", "[]" and "()"](http://www.codewars.com/kata/573d11c48b97c0ad970002d4)
 - [#41: Regular Expression--"\"](http://www.codewars.com/kata/573e6831e3201f6a9b000971)
 - [#42: Regular Expression--(?:), (?=) and (?!)](http://www.codewars.com/kata/573fb9223f9793e485000453)
 
"""

var a1="A",a2="a",b1="B",b2="b",c1="C",c2="c",d1="D",d2="d",e1="E",e2="e",n1="N",n2="n"
function Dad(){
  //select some variable to combine "Dad"
  return d1 +a2 +d2;
}
function Bee(){
  //select some variable to combine "Bee"
  return b1 +e2 + e2;
}
function banana(){
  //select some variable to combine "banana"
  return b2 + a2 + n2 + a2 + n2 + a2;
}

//responda a algunas preguntas si ha terminado los trabajos anteriores
function answer1(){
  //the answer should be "yes" or "no"
  return "no";
}
function answer2(){
  //the answer should be "yes" or "no"
  return "no";
}
function answer3(){
  //the answer should be "yes" or "no"
  return "yes";
}

