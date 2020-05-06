# ChaoXing_Downloader
## 简介：  
用于超星平台课程界面没有下载按钮的资源（包括PPT、MP4、MP3）的下载，基于selenium库，下载依赖于Chrome浏览器  
 
 
## 你需要：
①谷歌Chrome浏览器  
②Python  
③一两节课的Python基础


## 注意事项：
1. 爬虫跳不过登录这一步，仍需手动输入图形验证码。至于为什么不配上一个自动识别图形验证码的模块，因为我懒。
2. 本程序会下载页面中**所有**可下载的资源，如果只想下载单个文件请点[这里](http://www.baidu.com)
  
  
## 使用方法：
1. 查看自己谷歌浏览器版本号，找到对应版本的[Chromedriver](http://npm.taobao.org/mirrors/chromedriver/)下载并放在main.py所在文件夹中（[如何查找浏览器版本对应的driver](http://www.baidu.com)）
2. cmd运行 ``pip install selenium``
3. 在main.py文件中修改用户名、密码、下载地址 **【不要用平台登录】**
4. 运行main.py文件，在***终端终端终端***输入资源所在链接和登录时的验证码
5. 回车


## 作者：
BC  
有我微信的直接联系我就好
