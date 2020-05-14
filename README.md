# ChaoXing_Downloader
## 简介：  
用于超星平台课程界面没有下载按钮的资源（包括PPT、MP4、MP3）的下载，基于selenium库，下载依赖于Chrome浏览器  
  
[B站视频讲解说明](https://www.bilibili.com/video/BV1ug4y1B7p1)
 
 
 
 
## 你需要：
①谷歌Chrome浏览器  
②Python  
③一两节课的Python基础




## 注意事项：
1. 使用了 超级鹰 接码平台，实现了自动识别验证码功能，该接口需要付费，可自行注册购买，也可联系作者，作者账号还有免费额度
2. 本程序会下载页面中**所有**可下载的资源，如果只想下载单个文件请点[这里](http://www.baidu.com)
  
  
  
  
## 使用方法：
1. 查看自己谷歌浏览器版本号，找到对应版本的[Chromedriver](http://npm.taobao.org/mirrors/chromedriver/)下载并放在main.py所在文件夹中（[如何查找浏览器版本对应的driver](http://www.baidu.com)）
2. cmd运行 ``pip install -r requirements.txt``
3. 在超级鹰平台注册，并生成一个软件ID
4. 在main.py文件中修改超星的用户名、密码**【不要用平台登录】**、下载路径、超级鹰的用户名、密码、软件ID  
5. 运行main.py文件，在终端输入资源所在链接
6. 回车  




## 更新日志：
5/5/2020：  
	初步上传文件，可以下载课程页面的资源  

5/6/2020：  
	更新main.py文件，可以下载“资料”里的资源了  

5/8/2020：  
	上传chaojiying.py文件  
	更新main.py文件，可以自动识别验证码了



## 作者：
BC  
有我微信的直接联系我就好
