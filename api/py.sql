/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50617
Source Host           : localhost:3306
Source Database       : py

Target Server Type    : MYSQL
Target Server Version : 50617
File Encoding         : 65001

Date: 2017-03-24 17:04:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for daily
-- ----------------------------
DROP TABLE IF EXISTS `daily`;
CREATE TABLE `daily` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `text` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of daily
-- ----------------------------
INSERT INTO `daily` VALUES ('1', '2017-03-15', '一个web应用的架构应该包括哪些东西？是简单的（服务器，数据库，前端，后端），还是更详细的（从应用的功能设计开始，到网站功能的实现）\r\n\r\n服务器的安全应该做些什么预防\r\n\r\n怎么样去设计一个拓展性较强的数据库（可能某个大块需要添加一些扩展信息）\r\n\r\n如何设计一个多端通用的啊api');
INSERT INTO `daily` VALUES ('2', '2017-03-15', '# 你好这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨这是第二条碎语打算将打开拉萨');

-- ----------------------------
-- Table structure for link
-- ----------------------------
DROP TABLE IF EXISTS `link`;
CREATE TABLE `link` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `desc` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of link
-- ----------------------------
INSERT INTO `link` VALUES ('1', 'Ruke驿站', '我们来休息吧,一个程序员孤独的分享,垃圾网站,毁我青春', 'https://ruke.xyz', null);
INSERT INTO `link` VALUES ('2', 'Ruke.git', '我的另一个网站', 'https://ruker.top', null);
INSERT INTO `link` VALUES ('3', '九幽的博客', '二逼青年欢乐多', 'https://www.itnetve.top/', null);
INSERT INTO `link` VALUES ('4', '小艺博客', '一个小清新站点', 'https://blog.domeyi.com/', null);
INSERT INTO `link` VALUES ('5', '阿佩', '我常去的网站', 'https://www.xiaocp.com/', null);

-- ----------------------------
-- Table structure for menu
-- ----------------------------
DROP TABLE IF EXISTS `menu`;
CREATE TABLE `menu` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `pid` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of menu
-- ----------------------------
INSERT INTO `menu` VALUES ('1', '技术', '0');
INSERT INTO `menu` VALUES ('2', 'PHP', '1');
INSERT INTO `menu` VALUES ('3', 'Python', '1');
INSERT INTO `menu` VALUES ('4', 'javaScript', '1');
INSERT INTO `menu` VALUES ('5', 'Vue', '1');
INSERT INTO `menu` VALUES ('6', 'HTML&CSS', '1');
INSERT INTO `menu` VALUES ('7', '服务器', '1');
INSERT INTO `menu` VALUES ('8', '博客更新', '0');

-- ----------------------------
-- Table structure for oauth
-- ----------------------------
DROP TABLE IF EXISTS `oauth`;
CREATE TABLE `oauth` (
  `appid` varchar(255) NOT NULL,
  `secret` varchar(255) NOT NULL,
  PRIMARY KEY (`appid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oauth
-- ----------------------------
INSERT INTO `oauth` VALUES ('18500820754', '667bfb2d66fa79699ee2ace21d1863af');

-- ----------------------------
-- Table structure for posts
-- ----------------------------
DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `desc` text NOT NULL,
  `content` text NOT NULL,
  `menu_id` int(11) NOT NULL,
  `push_at` varchar(40) NOT NULL,
  `click_num` int(11) NOT NULL DEFAULT '1',
  `tags` varchar(255) NOT NULL,
  `img_url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of posts
-- ----------------------------
INSERT INTO `posts` VALUES ('1', '测试文章666666666666666666', '这是测试文化发发就上课了这是测试文化发发就上课了这是测试文化发发就上课了这是测试文化发发就上课了这是测试文化发发就上课了这是测试文化发发就上课了这是测试文化发发就上课了这是测试文化发发就上课了这是测试文化发发就上课了这是测试文化发发就上课了这是测试文化发发就上课了这是测试文化发发就上课了这是测试文化发发就上课了', '46546\n\n### 打算发大水\n\n', '8', '2017-03-12 14:50:12', '14', '5, 6, ,', '20170324153544.png');
INSERT INTO `posts` VALUES ('5', '使用uwsgi+nginx部署flask到服务器', '前端时间接触了Flask框架,想把他部署到服务器上,于是我在阿里云买了一天服务器一年,心痛(好贵),因为新的域名也刚刚备案好(到现在为止已经有3个备案了的域名了,可惜ruke.xyz在北京不能备案),前端使用vue实现,用MVVM架构来玩玩,顺便学学python和vue', '这是一片测试文章,我也很好奇这是为啥\n```python\nclass LinkAPI(MethodView):\n  decorators = [admin_api]\n\n  def get(self, id):\n    if id is None:\n      schema = LinkSchema(many=True)\n      res = schema.dump(Link.query.all())\n      return success(res.data)\n    else:\n      schema = LinkSchema()\n      res = schema.dump(Link.query.filter_by(id=id).first())\n      return success(res.data)\n\n  def post(self):\n    title = request.json.get(\'title\')\n    desc = request.json.get(\'desc\')\n    url = request.json.get(\'url\')\n    schema = LinkSchema()\n    has = schema.dump(Link.query.filter(or_(Link.title == title,Link.url == url)).first())\n    if has.data is None or len(has.data) == 0:\n      db.session.add(Link(title=title, url=url, desc=desc))\n      db.session.commit()\n    return success()\n\n  def put(self, id):\n    title = request.json.get(\'title\')\n    desc = request.json.get(\'desc\')\n    url = request.json.get(\'url\')\n    schema = LinkSchema()\n    has = schema.dump(Link.query.filter(or_(Link.title == title,Link.url == url)).filter(Link.id!=id).first())\n    if has.data is None or len(has.data) == 0:\n      n = Link.query.get(id)\n      n.title = title\n      n.url = url\n      n.desc = desc\n      db.session.commit()\n    return success()\n\n  def delete(self, id):\n    link = Link.query.get(id)\n    db.session.delete(link)\n    db.session.commit()\n    return success()\n```\n\n![图片](http://localhost:5000/static/20170323135851.png)\n\n### 当让建立科技含量打法发送旅客的附近啊离开大树发的时间里 经历多少空间\n\n```测试```', '3', '2017-03-23 13:59:25', '905', '16, 17, 18, 1,', '20170324144441.png');
INSERT INTO `posts` VALUES ('9', '使用python将excel数据导入到mysql', '昨天我们说了如何将mysql导入到excel,今天我们就讲讲简单的将excel数据导入到mysql\n\npython是使用模块xlrd来导入到mysql的,使用pymysql(python2.X的使用MySQLdb)来链接mysql数据库的', '```python\n# -*- coding: utf-8 -*-\nimport xlrd\nimport pymysql\n \n#设置基本变量\n_host = \'localhost\'\n_db = \'13net\'\n_user = \'root\'\n_password = \'root\'\n_table = \'net_members_bak\'\n_excel_name = \'./tes2t.xlsx\'\n \n#open excel\nexcel = xlrd.open_workbook(_excel_name)\nsheet = excel.sheet_by_index(0)\n \nrows = sheet.nrows\ncols = sheet.ncols\ndata = []\nfields=\'\'\n#创建好要数据,如果第一行是表头的话，从1开始，若第一行就是数据，从0开始\n#在这里有必要提醒大家的是,这只是个简单的数据处理,如果你的数据有一些特殊的字符,或者数据,需要先将数据处理好了之后再来打包导入\nfor i in range(1,rows):\n  data.append(sheet.row_values(i))\n \nfor i in range(0,cols):\n    fields = fields+\'%s,\'\nprint(fields)\n# mysql\nconn = pymysql.connect(host=_host,user=_user,password=_password,db=_db,charset=\'utf8\')\ncursor = conn.cursor()\n \n#个人觉得最好先创建好表之后来导入数据把，如果要新建的话，也可以在这执行语句新建，但是不建议这么做\n \n#批量插入数据\ncursor.executemany(\"insert into \"+_table+\" values(\"+fields[:-1]+\");\" ,data)\n#不要忘记commit\nconn.commit()\n```', '5', '2017-03-23 15:32:36', '15', '21,22,17,4,', '20170324141723.png');
INSERT INTO `posts` VALUES ('10', 'PHP中如何使用孔磊回家安徽EasyWechat,Wechat', '默认情况下图像将使用原始尺寸，但如果用 max-width: 100% 标签，则图像将沾满整个容器。默认情况下图像将使用原始尺寸，但如果用 max-width: 100% 标签，则图像将沾满整个容器。默认情况下图像将使用原始尺寸，但如果用 max-width: 100% 标签，则图像将沾满整个容器。默认情况下图像将使用原始尺寸，但如果用 max-width: 100% 标签，则图像将沾满整个容器。默认情况下图像将使用原始尺寸，但如果用 max-width: 100% 标签，则图像将沾满整个容器。默认情况下图像将使用原始尺寸，但如果用 max-width: 100% 标签，则图像将沾满整个容器。', '默认情况下图像将使用原始尺寸，但如果用 max-width: 100% 标签，则图像将沾满整个容器。默认情况下图像将使用原始尺寸，但如果用 max-width: 100% 标签，则图像将沾满整个容器。\n\n![图片](http://localhost:5000/static/20170324120335.png)\n\n这是测试```测试```\n\n### 别着急呀', '2', '2017-03-24 12:04:00', '13', '5,16,22,18,', '20170324120234.png');
INSERT INTO `posts` VALUES ('11', '使用python导出mysql数据到excel', '以前我们就提到过,使用php将数据导出到excel,有类库的话,也很简单,但是重点是真的很啰嗦 今天,看了一...以前我们就提到过,使用php将数据导出到excel,有类库的话,也很简单,但是重点是真的很啰嗦 今天,看了一...', '#### 不多讲废话,直接上代码\n\n```python\n# -*- coding: utf-8 -*-\nimport xlwt\nimport pymysql\n \n#设置基本变量\n_host = \'localhost\'\n_db = \'13net\'\n_user = \'root\'\n_password = \'root\'\n_table = \'net_members\'\n_excel_name = \'tes2t\'\n \n#注意编码\nconn = pymysql.connect(host=_host,user=_user,password=_password,db=_db,charset=\'utf8\')\ncursor = conn.cursor()\ncount = cursor.execute(\'select id,username,student_no from %s\'%_table);\nprint(\'has %s line\'%count);\n \n#重置游标\ncursor.scroll(0,mode=\'absolute\')\n \n#结果\nret = cursor.fetchall();\n \n#头部\nfields = cursor.description\n#创建excel\nexcel = xlwt.Workbook()\n#创建工作簿\nsheet = excel.add_sheet(_excel_name,cell_overwrite_ok=True)\n#写入字段名\nfor k,v in enumerate(fields):\n  sheet.write(0,k,v[0])\n#写入数据\nfor key,value in enumerate(ret):\n  for kk,vv in enumerate(value):\n    sheet.write(key+1,kk,vv)\n \nexcel.save(\'./%s.xlsx\'%_excel_name)\n```', '3', '2017-03-24 15:30:45', '13', '20,22,21,', '20170324152929.png');
INSERT INTO `posts` VALUES ('12', '这是有关服务器的文章', '测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据', '# 测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据测试数据,测试数据', '7', '2017-03-24 15:36:50', '10', '17,4,20,6,18,', '20170324153616.png');
INSERT INTO `posts` VALUES ('13', '我就是理发师的', 'dfasdf', 'fdasfsda', '6', '2017-03-24 15:38:26', '10', '5,6,18,22,', '');
INSERT INTO `posts` VALUES ('14', 'sssdfdsfasdfsadfsadfdsaf', 'dfdsfsda', 'fdasfadsfsadfsda', '4', '2017-03-24 15:38:39', '10', '5,16,18,22,', '');

-- ----------------------------
-- Table structure for post_tag
-- ----------------------------
DROP TABLE IF EXISTS `post_tag`;
CREATE TABLE `post_tag` (
  `post_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of post_tag
-- ----------------------------

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `add_at` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES ('1', 'Ajax', '2017-03-15 17:15:48');
INSERT INTO `tag` VALUES ('2', 'Html5', '2017-03-15 17:15:57');
INSERT INTO `tag` VALUES ('3', 'Laravel', '2017-03-15 17:16:14');
INSERT INTO `tag` VALUES ('4', 'ThinkPHP', '2017-03-15 17:16:17');
INSERT INTO `tag` VALUES ('5', 'ShadowSocket', '2017-03-15 17:48:34');
INSERT INTO `tag` VALUES ('6', 'Test Tag', '2017-03-15 17:49:04');
INSERT INTO `tag` VALUES ('15', '测试标签', '2017-03-20 16:32:59');
INSERT INTO `tag` VALUES ('16', 'Uwsgi', '2017-03-23 13:56:36');
INSERT INTO `tag` VALUES ('17', 'Nginx', '2017-03-23 13:56:48');
INSERT INTO `tag` VALUES ('18', 'Flask', '2017-03-23 13:57:00');
INSERT INTO `tag` VALUES ('19', '服务器', '2017-03-23 13:57:11');
INSERT INTO `tag` VALUES ('20', 'python', '2017-03-23 15:31:43');
INSERT INTO `tag` VALUES ('21', 'excel', '2017-03-23 15:31:53');
INSERT INTO `tag` VALUES ('22', 'mysql', '2017-03-23 15:32:00');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `sex` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'xiao ming', '1');
INSERT INTO `user` VALUES ('2', 'xiao hong ', '2');
