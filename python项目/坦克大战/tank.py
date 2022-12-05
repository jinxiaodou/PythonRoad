'''
坦克大战需求分析
1.坦克类（我方 敌方）
    射击
    移动
    显示坦克 我方坦克enter重生，esc暂停 开始
2.子弹类
    移动
    显示
    消失
3.墙壁类
    显示
    是否可以通过
    是否可以爆炸
    是否可以打掉
4.爆炸效果类
    展示效果
5.音效类   
    播放效果
6.主类
    开始游戏
    结束游戏
    退出
打包流程：
安装打包库
pip3 install PYInstaller
cd到项目路径
-F 打包单个文件，-D打包文件夹 -w 关闭命令行
PYInstaller -makespec -w xxx.py 生成spec文件，其中xxx.py是运行时程序的入口py文件。-w不打开console，-c打开console。
完成后删除生成的dist build文件夹
修改tank.spec 前置的几行
需要修改pathex的内容，写上所有py文件，和入口文件在一个目录的不用在前面加地址，否则要加绝对地址
datas中是资源文件夹的所处位置，写法类似于python元组
第一个参数：Python中的资源文件等非py类型文件的路径
第二个参数：打包后路径，要和路径中的文件夹名称相同
举例：
datas=[('D:\\intership\\generalExcel2Db\\images','images')],
excludes中是无需导入的第三方库，直接写第三库的名称即可
app中的name是生成的应用名
icon是应用图标 绝对路径
保存spec文件
PYInstaller xxx.spec
生成的dist文件夹中的有exe文件（mac是app格式）
'''
import pygame
import time
import random

SCREEN_WIDTH=500
SCREEN_HEIGHT=500
BG_COLOR=pygame.Color(0, 0, 0)
TEXT_COLOR=pygame.Color(255,0,0)
tankWidth=30
BULLET_SPEED=20

class MainGame():
    window=None
    my_tank=None
    # 敌方坦克列表
    eTankList=[]
    maxETank=6
    totalETank=8
    diedETank=0
    myBulletList=[]
    # 最多5颗子弹
    maxMyBulletCount=5
    # 敌方子弹
    enemyBulletList=[]
    explodeList=[]
    MyTankLiveCount=3
    wallList=[]
    pause=False
    successFlag=False

    def __init__(self):
        # 加载主窗口
        pygame.display.init()
        # 设置窗口的大小及显示
        MainGame.window=pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # 设置标题
        pygame.display.set_caption('坦克大战')
        # 初始化我方坦克
        self.createMyTank()
        self.createWalls()
        # 创建音乐 添加到对应播放通道进行播放
        bgm=Music('musics/bgm.wav')
        ch=pygame.mixer.Channel(0)
        bgm.play(ch)
        self.startGame()
    
    # 开始游戏
    def startGame(self): 
        while True:
            time.sleep(0.02)
            # 设置填充色
            MainGame.window.fill(BG_COLOR)
            self.getEvent()
            MainGame.window.blit(self.setText('敌方坦克剩余数量：%d'%(MainGame.totalETank-MainGame.diedETank)), (10,10))
            # 初始化敌方坦克
            self.createEnemyTanks()
            if MainGame.my_tank!=None and MainGame.my_tank.live:
                MainGame.my_tank.display()
            else:
                del MainGame.my_tank
                MainGame.my_tank=None
            self.displayEnemyTank()
            self.blitMyBullet()
            self.blitEnemyBullet()
            self.blitExplode()
            self.blitWalls()
            if MainGame.my_tank!=None and MainGame.my_tank.live and not MainGame.my_tank.stop:
                MainGame.my_tank.move()
            if MainGame.successFlag:
                MainGame.window.blit(self.setText('恭喜你胜利了', 30), (200,200))
            pygame.display.update()

    # 创建我方坦克
    def createMyTank(self):
        if MainGame.MyTankLiveCount<=0:
            # 复活次数用尽，结束游戏
            print('复活次数用尽')
        else:
            MainGame.my_tank=MyTank((SCREEN_WIDTH-tankWidth)/2, SCREEN_HEIGHT-tankWidth)
            music=Music('musics/life.mp3')
            ch=pygame.mixer.Channel(1)
            music.play(ch)
            MainGame.MyTankLiveCount-=1

    # 创建敌方坦克
    def createEnemyTanks(self):
        count=MainGame.totalETank-MainGame.diedETank
        if count<=0:
            self.setSuccess(True)
            return
        if count>MainGame.maxETank:
            count=MainGame.maxETank
        for i in range(count-len(MainGame.eTankList)):
            left=random.randint(0, SCREEN_WIDTH-tankWidth)
            speed=random.randint(1, 3)
            MainGame.eTankList.append(EnemyTank(left, 0, speed*2)) 

    # 显示敌方坦克
    def displayEnemyTank(self):
        for etank in MainGame.eTankList:
            if etank.live:
                etank.display()
                etank.move()
                eBullet=etank.shot()
                if eBullet!=None:
                    MainGame.enemyBulletList.append(eBullet)

    # 绘制我方子弹
    def blitMyBullet(self):
        for bullet in MainGame.myBulletList:
            if bullet.live:
                bullet.display()
                bullet.move()
                bullet.hitEnemyTank()
                bullet.hitWall()
                bullet.hitEnemyBullet()
            else:
                MainGame.myBulletList.remove(bullet)

    # 绘制敌方子弹
    def blitEnemyBullet(self):
        for bullet in MainGame.enemyBulletList:
            if bullet.live:
                bullet.display()
                bullet.move()
                bullet.hitMyTank()
                bullet.hitWall()
            else:
                MainGame.enemyBulletList.remove(bullet)

    # 绘制爆炸
    def blitExplode(self):
        for explode in MainGame.explodeList:
            if explode.live:
                explode.display()
            else:
                MainGame.explodeList.remove(explode)

    # 创建墙壁
    def createWalls(self):
        for i in range(8):
            for j in range(4):
                wall1=Wall(i*80+0, 100+j*100)
                wall2=Wall(i*80+16, 100+j*100)
                wall3=Wall(i*80+0, 116+j*100)
                wall4=Wall(i*80+16, 116+j*100)
                MainGame.wallList.append(wall1)
                MainGame.wallList.append(wall2)
                MainGame.wallList.append(wall3)
                MainGame.wallList.append(wall4)

    # 绘制墙壁
    def blitWalls(self):
        for wall in MainGame.wallList:
            if wall.live:
                wall.display()
            else:
                MainGame.wallList.remove(wall)

    # 暂停游戏 按ESC暂停开始
    def pauseGame(self):
        MainGame.pause=not MainGame.pause
        if MainGame.pause:
            pygame.mixer.pause()
        else:
            pygame.mixer.unpause()
    
    # 游戏胜利
    def setSuccess(self, success):
        if MainGame.successFlag!=success:
            MainGame.successFlag=success
            music=Music('musics/success.wav')
            ch=pygame.mixer.Channel(0)
            music.play(ch)
    
    # 结束游戏
    def endGame(self):
        print('谢谢使用，欢迎再来')
        exit()

    # 设置文字
    def setText(self, text, size=18):
        # 初始化字体
        pygame.font.init()
        # 查看所有字体
        # print(pygame.font.get_fonts())
        # 获取字体font对象
        font=pygame.font.SysFont('songti', size)
        # 绘制文本
        textSurface=font.render(text, True, TEXT_COLOR)
        return textSurface

    # 获取事件
    def getEvent(self):
        # 获取所有事件
        eventList=pygame.event.get()
        for event in eventList:
            if event.type==pygame.QUIT:
                # 关闭窗口
                self.endGame()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if MainGame.my_tank!=None and MainGame.my_tank.live:
                        MainGame.my_tank.direction='L'
                        MainGame.my_tank.stop=False
                        music=Music('musics/move.mp3')
                        ch=pygame.mixer.Channel(2)
                        music.play(ch,-1)
                elif event.key==pygame.K_RIGHT:
                    if MainGame.my_tank!=None and MainGame.my_tank.live:
                        MainGame.my_tank.direction='R'
                        MainGame.my_tank.stop=False
                        music=Music('musics/move.mp3')
                        ch=pygame.mixer.Channel(2)
                        music.play(ch,-1)
                elif event.key==pygame.K_UP:
                    if MainGame.my_tank!=None and MainGame.my_tank.live:
                        MainGame.my_tank.direction='U'
                        MainGame.my_tank.stop=False
                        music=Music('musics/move.mp3')
                        ch=pygame.mixer.Channel(2)
                        music.play(ch,-1)
                elif event.key==pygame.K_DOWN:
                    if MainGame.my_tank!=None and MainGame.my_tank.live:
                        MainGame.my_tank.direction='D'
                        MainGame.my_tank.stop=False
                        music=Music('musics/move.mp3')
                        ch=pygame.mixer.Channel(2)
                        music.play(ch,-1)
                elif event.key==pygame.K_SPACE:
                    if MainGame.my_tank!=None and MainGame.my_tank.live and len(MainGame.myBulletList)<MainGame.maxMyBulletCount:
                        bullet=MainGame.my_tank.shot()
                        MainGame.myBulletList.append(bullet)
                elif event.key==pygame.K_RETURN:
                    # 回车键重生
                    self.createMyTank()
                elif event.key==pygame.K_ESCAPE:
                    self.pauseGame()
            elif event.type==pygame.KEYUP:
                if MainGame.my_tank!=None and MainGame.my_tank.live:
                    if event.key==pygame.K_LEFT and MainGame.my_tank.direction=='L':
                        MainGame.my_tank.stop=True
                        ch=pygame.mixer.Channel(2)
                        ch.stop()
                    elif event.key==pygame.K_RIGHT and MainGame.my_tank.direction=='R':
                        MainGame.my_tank.stop=True
                        ch=pygame.mixer.Channel(2)
                        ch.stop()
                    elif event.key==pygame.K_UP and MainGame.my_tank.direction=='U':
                        MainGame.my_tank.stop=True
                        ch=pygame.mixer.Channel(2)
                        ch.stop()
                    elif event.key==pygame.K_DOWN and MainGame.my_tank.direction=='D':
                        MainGame.my_tank.stop=True
                        ch=pygame.mixer.Channel(2)
                        ch.stop()

# 精灵基类
class BaseClass(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

# 坦克基类
class Tank(BaseClass):
    def __init__(self, left, top):
        self.images={
            'U': pygame.image.load('images/pltankU.png'),
            'D': pygame.image.load('images/pltankD.png'),
            'L': pygame.image.load('images/pltankL.png'),
            'R': pygame.image.load('images/pltankR.png'),
            }
        # 方向
        self.direction='U'
        # 根据当前图片的方向获取图片
        self.image=self.images[self.direction]
        # 获取区域
        self.rect=self.image.get_rect()
        # 设置区域的left和top
        self.rect.left=left
        self.rect.top=top
        # 速度
        self.speed=5
        self.stop=True
        self.live=True
        self.oldLeft=self.rect.left
        self.oldTop=self.rect.top

    # 移动
    def move(self):
        self.oldLeft=self.rect.left
        self.oldTop=self.rect.top
        # 判断坦克的方向进行移动
        if self.direction=='L':
            if self.rect.left>0:
                self.rect.left-=self.speed
        elif self.direction=='R':
            if (self.rect.left+self.rect.width)<SCREEN_WIDTH:
                self.rect.left+=self.speed
        elif self.direction=='U':
            if self.rect.top>0:
                self.rect.top-=self.speed
        elif self.direction=='D':
            if (self.rect.top+self.rect.height)<SCREEN_HEIGHT:
                self.rect.top+=self.speed
        # 不让超出边界
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.left>(SCREEN_WIDTH-self.rect.width):
            self.rect.left=(SCREEN_WIDTH-self.rect.width)
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.top>(SCREEN_HEIGHT-self.rect.height):
            self.rect.top=SCREEN_HEIGHT-self.rect.height
        # 不可穿过墙壁
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self, wall):
                # if isinstance(self, MyTank):
                    # print(self.rect)
                self.rect.left=self.oldLeft
                self.rect.top=self.oldTop
                return
        
    # 射击
    def shot(self):
        bullet=Bullet(self)
        return bullet

    # 展示
    def display(self):
        # 获取展示对象
        self.image=self.images[self.direction]
        # blit方法去展示
        MainGame.window.blit(self.image, self.rect)

    # 停顿
    def stay(self):
        self.rect.left=self.oldLeft
        self.rect.top=self.oldTop
    
# 我方坦克类
class MyTank(Tank):
    def __init__(self,left,top):
        super(MyTank, self).__init__(left, top)

    # 移动
    def move(self):
        if MainGame.pause:
            return
        super(MyTank, self).move()
        self.isTankHit()

    # 检测是否与坦克碰撞
    def isTankHit(self):
        for eTank in MainGame.eTankList:
            if pygame.sprite.collide_rect(eTank, self):
                self.stay()

    # 射击
    def shot(self):
        if MainGame.pause:
            return
        bullet=Bullet(self)
        music=Music('musics/biu.mp3')
        ch=pygame.mixer.Channel(3)
        music.play(ch)
        return bullet

# 敌方坦克类
class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        super(EnemyTank, self).__init__(left, top)
        # 加载图片
        self.images={
            'U': pygame.image.load('images/eTank01_N_U.png'),
            'D': pygame.image.load('images/eTank01_N_D.png'),
            'L': pygame.image.load('images/eTank01_N_L.png'),
            'R': pygame.image.load('images/eTank01_N_R.png'),
        }
        # 方向随机
        self.direction=self.randDirection()
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.speed=speed
        self.stop=True
        self.step=random.randint(10, 100)
    
    # 随机方向
    def randDirection(self):
        if MainGame.pause:
            return
        self.step=random.randint(10, 100)
        return(random.choice(['U','L','D','R']))

    # 移动
    def move(self):
        if MainGame.pause:
            return
        self.step-=1
        if (self.direction=='L' and self.rect.left<=0) or (self.direction=='R' and self.rect.left>=(SCREEN_WIDTH-self.rect.width)) or (self.direction=='U' and self.rect.top<=0) or (self.direction=='D' and self.rect.top>=(SCREEN_HEIGHT-self.rect.height)) or self.step<=0:
            self.direction=self.randDirection()
        Tank.move(self)
        if self.rect.left==self.oldLeft and self.rect.top==self.oldTop:
            self.direction=self.randDirection()
        if MainGame.my_tank!=None and MainGame.my_tank.live and pygame.sprite.collide_rect(MainGame.my_tank, self):
            self.stay()
    
    # 射击
    def shot(self):
        if MainGame.pause:
            return
        # 随机射击
        num=random.randint(1, 100)
        if num<2:
            return Bullet(self)

# 子弹类
class Bullet(BaseClass):
    def __init__(self,tank):
        self.speed=BULLET_SPEED
        self.direction=tank.direction
        self.images={
            'U': pygame.image.load('images/bulletU.png'),
            'D': pygame.image.load('images/bulletD.png'),
            'L': pygame.image.load('images/bulletL.png'),
            'R': pygame.image.load('images/bulletR.png'),
        }
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()
        if self.direction=='L':
            self.rect.left=tank.rect.left+self.rect.width
            self.rect.top=tank.rect.top+(tank.rect.height-self.rect.height)/2
        elif self.direction=='R':
            self.rect.left=tank.rect.left+tank.rect.width
            self.rect.top=tank.rect.top+(tank.rect.height-self.rect.height)/2
        elif self.direction=='D':
            self.rect.left=tank.rect.left+(tank.rect.width-self.rect.width)/2
            self.rect.top=tank.rect.top+tank.rect.height
        elif self.direction=='U':
            self.rect.left=tank.rect.left+(tank.rect.width-self.rect.width)/2
            self.rect.top=tank.rect.top+self.rect.height
        self.live=True

    # 移动
    def move(self):
        if MainGame.pause:
            return
        # 判断子弹的方向进行移动
        if self.direction=='L':
            self.rect.left-=self.speed
        elif self.direction=='R':
            self.rect.left+=self.speed
        elif self.direction=='U':
            self.rect.top-=self.speed
        elif self.direction=='D':
            self.rect.top+=self.speed
        # 碰到墙壁消失
        if self.rect.left<0 or self.rect.left>SCREEN_WIDTH or self.rect.top<0 or self.rect.top>SCREEN_HEIGHT:
            self.live=False

    # 显示
    def display(self):
        MainGame.window.blit(self.image, self.rect)

    # 检测击中敌方坦克
    def hitEnemyTank(self):
        for enemyTank in MainGame.eTankList:
            if pygame.sprite.collide_rect(enemyTank, self):
                self.live=False
                enemyTank.live=False
                # 爆炸效果
                explode=Explode(enemyTank)
                MainGame.explodeList.append(explode)
                MainGame.eTankList.remove(enemyTank)
                MainGame.diedETank+=1

    # 检测击中我方坦克
    def hitMyTank(self):
        if MainGame.my_tank!=None and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(MainGame.my_tank, self):
                self.live=False
                MainGame.my_tank.live=False
                explode=Explode(MainGame.my_tank)
                MainGame.explodeList.append(explode)

    # 检测击中墙壁
    def hitWall(self):
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(wall, self):
                self.live=False
                wall.hp-=1
                if wall.hp==0:
                    wall.live=False

    # 检测是否击中敌方子弹
    def hitEnemyBullet(self):
        if MainGame.my_tank!=None and MainGame.my_tank.live:
            for enemyBullet in MainGame.enemyBulletList:
                if pygame.sprite.collide_rect(enemyBullet, self):
                    self.live=False
                    enemyBullet.live=False
                    MainGame.enemyBulletList.remove(enemyBullet)
                    MainGame.myBulletList.remove(self)
# 墙壁类
class Wall(BaseClass):
    def __init__(self,left,top):
        self.image=pygame.image.load('images/wall_H.png')
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.live=True
        self.hp=3

    def display(self):
        MainGame.window.blit(self.image, self.rect)

# 爆炸效果类
class Explode():
    def __init__(self,tank):
        self.images=[
            pygame.image.load('images/explode01.png'),
            pygame.image.load('images/explode02.png'),
            pygame.image.load('images/explode03.png')
        ]
        self.rect=tank.rect
        self.step=0
        self.image=self.images[self.step]
        self.live=True
        music=Music('musics/boom.wav')
        ch=pygame.mixer.Channel(4)
        music.play(ch)

    def display(self):
        if MainGame.pause:
            return
        if self.step<len(self.images):
            self.image=self.images[self.step]
            self.step+=1
        else:
            self.live=False
            self.step=0
        MainGame.window.blit(self.image, self.rect)

# 音效类
class Music():
    def __init__(self,filename):
        self.filename=filename
        pygame.mixer.init()
        self.sound=pygame.mixer.Sound(self.filename)
        # pygame.mixer.music.load(self.filename)

    def play(self,channel,loops=0):
        channel.play(self.sound,loops)

if __name__=='__main__':
    MainGame().__init__()