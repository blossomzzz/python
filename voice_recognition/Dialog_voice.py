# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication
from aip import AipSpeech#百度的API调用
import sys, pyaudio, wave, datetime, webbrowser, urllib.parse
from PyQt5 import QtCore, QtGui, QtWidgets

class Speech_Recognition_Thread(QThread):
    finished_signal = pyqtSignal(str)
    voice_signal = pyqtSignal(dict)

#参数设置
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    WAVE_OUTPUT_FILENAME = "output.wav"
    APP_ID = '11094970'
    API_KEY = 'tzi9Cz4SNSEZDtTQYjGGddKi'
    SECRET_KEY = 'vx1FvGoiMGODT2xg2c90sGPndppvAiwG'
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def __init__(self, v, parent = None):
        super().__init__(parent)
        self.RECORD_SECONDS = v

    # 读取文件
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def run(self):

        p = pyaudio.PyAudio()

        stream = p.open(format = self.FORMAT,
                        channels = self.CHANNELS,
                        rate = self.RATE,
                        input = True,
                        frames_per_buffer = self.CHUNK)

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        self.finished_signal.emit(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t问题采集完毕！')
        self.finished_signal.emit(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t语音识别中...！')
        # 识别本地文件
        voice = self.aipSpeech.asr(self.get_file_content('output.wav'), 'wav', 16000, {
            'lan': 'zh',
        })
        self.voice_signal.emit(voice)
        if voice['err_no'] == 0:
                webbrowser.open('https://baidu.com/s?wd=' + urllib.parse.quote(str(voice['result'])[2:-3]), new=2, autoraise=True)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 279)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "语音识别工具"))
        self.label.setText(_translate("Dialog", "录音时长："))
        self.pushButton.setText(_translate("Dialog", "问题采集"))


class Dialog_voice(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog_voice, self).__init__(parent)
        self.setupUi(self)
    
    def _show_message(self, message):
        if isinstance(message, str):
            self.textBrowser.append(message)
        elif isinstance(message, dict):
            if message['err_no'] == 0:
                self.textBrowser.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t问题是：' + str(message['result'])[2:-3])
                self.textBrowser.append('################################################################\n')
            else:
                self.textBrowser.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t我已经尽力了，问题解析失败！' + '错误代码：' + str(message['err_no']))
                self.textBrowser.append('################################################################\n')
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.textBrowser.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t问题采集中...')
        self.speech = Speech_Recognition_Thread(self.spinBox.value())
        self.speech.finished_signal.connect(self._show_message)
        self.speech.voice_signal.connect(self._show_message)
        self.speech.start()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    dialog = Dialog_voice()
    dialog.show()
    sys.exit(app.exec_())
