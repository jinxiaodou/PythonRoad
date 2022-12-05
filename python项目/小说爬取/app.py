from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QDesktopWidget, 
    QHBoxLayout, 
    QVBoxLayout,
    QPushButton, 
    QLineEdit, 
    QTableWidget, 
    QTableWidgetItem, 
    QLabel,
    QTextBrowser,
    QProgressBar)
from PyQt5.QtCore import QRect
import search,writeFile
import os, sys, time, random, threading

BASE_DIR=os.path.dirname(os.path.realpath(sys.argv[0]))

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('小说爬虫')
        self.resize(1080, 960)
        # 窗体位置
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        self.searchObj=None
        self.novelObj=None
        self.chapterObj=None
        self.article=None
        self.chapterWindow=None
        self.articleWindow=None
        self.pv=0
        # 垂直方向的布局
        VLayout=QVBoxLayout()
        VLayout.addLayout(self.init_search())
        VLayout.addLayout(self.init_table())
        VLayout.addLayout(self.init_progress())
        VLayout.addLayout(self.init_footer())
        self.setLayout(VLayout)

    def init_search(self):
        # 搜索布局
        search_layout=QHBoxLayout()
        self.search_input=QLineEdit()
        self.search_input.setPlaceholderText('请输入小说名')
        search_layout.addWidget(self.search_input)

        self.search_btn=QPushButton('搜索')
        self.search_btn.clicked.connect(lambda: self.search_action(self.search_input.text()))
        search_layout.addWidget(self.search_btn)
        return search_layout
    
    def init_table(self):
        # 表格布局
        table_layout=QHBoxLayout()
        self.table_widget=QTableWidget()       
        table_layout.addWidget(self.table_widget)
        return table_layout

    def init_progress(self):
        progress_layout=QHBoxLayout()
        self.progress_widget=QProgressBar()   
        self.progress_widget.setValue(self.pv)
        self.progress_widget.setMinimum(0)
        self.progress_widget.setMaximum(100)
        progress_layout.addWidget(self.progress_widget)
        return progress_layout

    def init_footer(self):
        # 底部布局
        footer_layout=QHBoxLayout()
        self.label_status=QLabel('待输入')
        footer_layout.addWidget(self.label_status)

        footer_layout.addStretch()

        self.download_btn=QPushButton('下载')
        self.download_btn.clicked.connect(lambda: self.download())
        footer_layout.addWidget(self.download_btn)

        return footer_layout
    
    def search_action(self, keyword):
        thread_search=threading.Thread(target=self.search, args=(keyword, ))
        thread_search.start()
        thread_search.join()
        self.show_novel()

    def search(self, keyword):
        self.label_status.setText('搜索中...')
        self.searchObj=search.NovelSearch(keyword)
        self.label_status.setText('请点击搜素结果')

    def show_novel(self):
        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(len(self.searchObj.novel_list))

        item1=QTableWidgetItem()
        item1.setText('序号')
        self.table_widget.setHorizontalHeaderItem(0, item1)

        item2=QTableWidgetItem()
        item2.setText('作品名称')
        self.table_widget.setHorizontalHeaderItem(1, item2)
        self.table_widget.setColumnWidth(1, 200)

        item3=QTableWidgetItem()
        item3.setText('作者')
        self.table_widget.setHorizontalHeaderItem(2, item3)
        self.table_widget.setColumnWidth(2, 200)
        # 绑定item点击事件
        self.table_widget.itemClicked.connect(self.select_novel)
        i=0
        for book in self.searchObj.novel_list:
            itemNum=QTableWidgetItem()
            itemNum.setText(book['num'])
            self.table_widget.setItem(i, 0, itemNum)
            
            itemName=QTableWidgetItem()
            itemName.setText(book['name'])
            self.table_widget.setItem(i, 1, itemName)

            itemAuthor=QTableWidgetItem()
            itemAuthor.setText(book['author'])
            self.table_widget.setItem(i, 2, itemAuthor)
            
            i+=1

    def write_novel(self, num):
        art=self.novelObj.choose_chapter(num)
        writeFile.writeToFile(art.bookname,  art.chaptername+'\n\n\n'+art.article)

    def select_novel(self, item):
        thread_novel=threading.Thread(target=self.get_chapters, args=(item,))
        thread_novel.start()
        thread_novel.join()
        self.show_chapter()

    def get_chapters(self, item):
        row = item.row()  # 获取行数
        self.label_status.setText('搜索中...')
        self.novelObj=self.searchObj.choose_novel(row)
        self.label_status.setText('请点击章节查看，或者直接下载全部')
    
    def show_chapter(self):
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(len(self.novelObj.chapter_list))
        
        item1=QTableWidgetItem()
        item1.setText('序号')
        self.table_widget.setHorizontalHeaderItem(0, item1)

        item2=QTableWidgetItem()
        item2.setText('章节')
        self.table_widget.setHorizontalHeaderItem(1, item2)
        self.table_widget.setColumnWidth(1, 300)

        # 绑定item点击事件
        self.table_widget.itemClicked.disconnect()
        self.table_widget.itemClicked.connect(self.select_chapter)
        i=1
        for chapter in self.novelObj.chapter_list:
            itemNum=QTableWidgetItem()
            itemNum.setText(str(i))
            self.table_widget.setItem(i, 0, itemNum)
            
            itemName=QTableWidgetItem()
            itemName.setText(chapter['name'])
            self.table_widget.setItem(i, 1, itemName)
            i+=1

    def select_chapter(self, item):
        threading_article=threading.Thread(target=self.get_article, args=(item,))
        threading_article.start()
        threading_article.join()
        str=self.article.chaptername+'\n\n\n'+self.article.article
        self.articleWindow=ArticleWindow(str)
        self.articleWindow.show()

    def get_article(self, item):
        row = item.row()  # 获取行数
        self.article=self.novelObj.choose_chapter(row-1)
    
    def download(self):
        length=len(self.novelObj.chapter_list)
        for i in range(length):
            threading_download=threading.Thread(target=self.write_novel, args=(i, ))
            threading_download.start()
            threading_download.join()
            self.pv=int((i+1)/(length))
            self.progress_widget.setValue(self.pv)
            sys.stdout.write('已下载第%d章：%d%%' % (i+1,self.pv*100) + '\r')
            sys.stdout.flush()
            time.sleep(random.randint(0,100)/100.0)

class ArticleWindow(QWidget):
    def __init__(self, str):
        super().__init__()
        layout=QVBoxLayout()
        self.textBrowser=QTextBrowser()
        self.textBrowser.setText(str)
        self.resize(800, 600)
        layout.addWidget(self.textBrowser)
        self.setLayout(layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()

    sys.exit(app.exec_())
