import re
# 一、some function
# 1.match:start to head,return re.Match
s='hello world'
result=re.match('he',s)
print(result.group())
# span:get the position
print(result.span())
# 2.search:just find one,return re.Match
result1=re.search('wor',s)
print(type(result1))
print(result.span())
print(result.group())
# 3.findall:find all,return a list
s2='hello world,hello world'
result3:list=re.findall('he',s2)
print(result3)

# 二、regular expression
# 1.str that is attached to 'r' means that the str is a normal str
print('hello \n word')
print(r'hello \n world')
# find numbers
s = '123455@qq.com!~'
result5=re.findall(r'\d',s)
print(result5)
# 2.find special character
s1 = '123455@qq.com!~'
result6=re.findall(r'\W',s)
print(result6)
# find letter
result7=re.findall(r'[a-zA-Z]',s1)
print(f'letter:{result7}')
# *:>=n  +:>=1  ?:<=1  {n,m}:n~m
# ^:match the start  $:match the end  \b:match Word of boundary
# |:match expression left of right  ():Parentheses character as a group
# match the account (consist of num and letter,just 6~10)
s3='addpd904'
# sfhfas_ is fail to meet the re
r='^[0-9a-zA-Z]{6,10}$'
result8=re.findall(r,s3)
print(result8)
# match QQ(5~11,the first number is not 0)
r2='^[1-9][0-9]{4,10}$'
s4='2945348232'
result9=re.findall(r2,s4)
print(f'qq:{result9}')
# macth e-mail
# findall will show all group (Parentheses re)
r4=r'^([\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+)$'
s5='eeew.ttee.fg@qq.com'
result10=re.findall(r4,s5)
print(f'email:{result10}')
print(result10)