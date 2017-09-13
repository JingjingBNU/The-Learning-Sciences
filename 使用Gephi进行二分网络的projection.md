# 使用Gephi进行二分网络的projection

请大家使用**data**文件夹中两份数据，进行可视化和转换。
可下载视频学习如何使用Gephi：
![twomodeprojection.mp4](../images/projection/twomodeprojection.mp4) 


## 数据导入Gephil

将数据导入Gephi在开始界面点击**新建项目**创建一个新的项目。在**数据资料（Data Laboratory）**界面选择**输入电子表格（Import Spreadsheet）**，弹出如下对话框：

![][1]

[1]:
images/projection/import.png


### 导入节点列表选择需要导入的节点列表文件（CSV格式），分隔符（Sepatator）选择逗号（Comma），如表格（As table）选择节点表格（Nodes table），点击下一步，出现如下对话框，输入列中的Cat变量一栏设置为String格式（这对于后面区分两类节点有重要作用）：

![][2]

[2]:
images/projection/nodelist.png


### 导入边列表选择需要导入的节点列表文件（CSV格式），分隔符选择逗号（Sepatator），如表格（As table）一项要选择边表格（Edges table），点击下一步，出现如下对话框，输入列中的Type变量一栏设置为String格式，不用勾选“创建丢失节点（Creating missing nodes）”一项：

![][3]

[3]:
images/projection/edgelist.png


### 外观调整#### 节点大小调整
在外观界面，在节点大小（Ranking）选项下（即上图所示的钻石状按钮），可以根据节点的度等设置节点大小范围。
![][4]

[4]:
images/projection/nodesize.png


#### 节点颜色调整同样，在节点颜色（Partition）选项下，可以根据Cat一栏（即节点类型）来对节点的颜色进行设置并应用，以区分两种不同类型的节点。在外观面板同样可以对边的进行调整。

![][5]

[5]:
images/projection/nodecolour.png

#### 设置布局在左下角的布局界面，选择布局。选择**Force Atlas 2**算法布局，对布局属性进行调整，如点击**防止重叠**，**缩放**设为50等。
![][6]

[6]:
images/projection/layout.png

### 二分网络投影到单分图网络：在工具-插件中下载**MultiMode Networks Transformation Plugin**插件，在右侧**MultiMode Networks Projection**面板点击**加载属性（load attributes）**，如图所示：

![][7]

[7]:
images/projection/multi.png

Attribute type选择Cat(String),Left matrix与Right matrix二者的格式必须是对称的，如discipline的单分网络就是Left matrix选择discipline-academic，同时Right matrix选择academic-discipline。同时勾选“Remove Edges” 和 “Remove Nodes”两项（目的是去除原二分网络中的节点与连边，显示更清晰一些）点击运行，得到discipline单顶点网络。用同样的方法也可做academic即另外一类的单顶点网络图。
![][8]

[8]:
images/projection/click.png
