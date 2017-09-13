# 数据准备过程中的常见错误

### 主要存在的问题
> 数据列表中的分隔符是大家手动敲进去的，出现了中文的逗号，冒号，还有空格。这是数据整理过程中的大忌。在大数据的时代，人其实不能胜任简单的数据处理工作，在数据处理工作中，会更容易出现错误，这些错误会导致后面的分析无法正常进行。格式化的数据中的标识符一定是自动生成的，保证不会因为疲劳，三心二意而出现如上的错误。

#### 与数据格式不匹配的多列

![][1]

[1]:
../images/mergedata/multiplecol.png


#### 出现中文逗号

![][2]

[2]:
../images/mergedata/chinese.png

#### 不检查不知道，一查有331个中文逗号，大家敲的累，数据清理工作更加累

![][3]

[3]:
../images/mergedata/331-comma.png

#### 标识符消失了

![][4]

[4]:
../images/mergedata/missing.png

#### 冒号也来凑热闹

![][5]

[5]:
../images/mergedata/semic.png




#### 英文逗号前出现空格

![][6]

[6]:
../images/mergedata/40-space.png

#### 出现不同的类别

![][6]

[6]:
../images/mergedata/more.png

#### 拼写错误，直接导致机器认为它是一个新类别

![][6]

[6]:
../images/mergedata/spell.png

#### oh, my god 这里也是拼写错误

![][6]

[6]:
../images/mergedata/spella.png

#### 漏填，找的我好辛苦
![][6]

[6]:
../images/mergedata/missingc.png
