from unicodedata import normalize, name
import unicodedata
import string

"""
U+0301 是 COMBINING ACUTE ACCENT
U+0301 是 组合用锐音符
"""
s1 = 'café'
s2 = 'cafe\u0301'
# print(s1==s2)
# print(len(s1), len(s2))
"""
NFC是把组合起来的字符看做一个码位
NFD是把每一个单独拆分开来计算码位
"""
# print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
# print(len(normalize('NFD', s2)), len(normalize('NFD', s1)))
# 使用函数规范之后s1和s2的码位相等之后Python才视为其相等
# print(len(normalize('NFC', s1)) == len(normalize('NFC', s2)))
# print(len(normalize('NFD', s2)) == len(normalize('NFD', s1)))


# half = '½'
# print(normalize('NFKC', half))
# four_squared = '4²'
# print(normalize('NFKC', four_squared))
# 注 8：微符号是“兼容字符”，而欧姆符号不是，这还真是奇怪。因此，NFC 不会改动微符号，但是会把欧
# 姆符号改成大写的欧米加；而 NFKC 和 NFKD 会把欧姆和微符号都改成其他字符。
# 文本和字节序列 ｜ 101
# micro = 'µ'
# micro_kc = normalize('NFKC', micro)
# print(micro, micro_kc)
# print(micro == micro_kc)
# print(ord(micro), ord(micro_kc))
# print(name(micro), name(micro_kc))


# s.lower和str.casefold()的区别:casefold()对于非中英文的其他语言小写有效

a = unicodedata.normalize('NFD', s1)
for i in a:
    print(unicodedata.combining(i))

# string.ascii_letters生成所有字母（a-z,A-Z)
# string.digits生成所有数字（0-9）

# str.maketrans：用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，
# 第二个参数也是字符串表示转换的目标。两个字符串的长度必须相同，为一一对应的关系。
# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)
# str = "this is string example....wow!!!"
# print(str.translate(trantab))

# Windows-1252 或 CP-1252 是拉丁字母的字符编码
# sorted排序函数
# setlocale 设置或读取地域化信息
# LC_COLLATE 字符串比较。
# pt_BR葡萄牙


# isidentifier() 方法用于判断字符串是否是有效的 Python 标识符，可用来判断变量名是否合法
# print( "if".isidentifier() )
# print( "def".isidentifier() )
# print( "class".isidentifier() )
# print( "_a".isidentifier() )
# print( "中国123a".isidentifier() )
# print( "123".isidentifier() )
# print( "3a".isidentifier() )
# print( "".isidentifier() )

# 判断字符串中所有字符是否都是可打印字符(in repr())或字符串为空
# print("oiuas\tdfkj".isprintable())  # 制表符 False
# print("oiuas\ndfkj".isprintable())  # 换行符 False
#
# print('oiu.123'.isprintable())  # True
# print('oiu 123'.isprintable())  # True
# print('~'.isprintable())  # True
# print(''.isprintable())  # True


