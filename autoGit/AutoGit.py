import os
import shutil

#�г���ǰĿ¼�µ��ļ����ļ��� D:\myworkspace\web\web-vehicle-center-vue
#Դ�ļ���
vehiclePath ="D:\\myworkspace\\web\\web-vehicle-center-vue"
# dir = os.listdir(filepath)

#��ģ�����ļ���·��
portalPath = "D:\\myworkspace\\web\\web-portal-vue"
sysconfigPath = "D:\\myworkspace\\web\\web-sysconfig-center-vue"
messagePath = "D:\\myworkspace\\web\\web-message-center-vue"
equipPath = "D:\\myworkspace\\web\\web-equip-center-vue"
personalPath = "D:\\myworkspace\\web\\web-personal-center-vue"
safetyPath = "D:\\myworkspace\\web\\web-safety-center-vue"
visitorPath = "D:\\myworkspace\\web\\web-visitor-center-vue"
accountPath = "D:\\myworkspace\\web\\web-account-center-vue"
unifiedportaPath = "D:\\myworkspace\\web\\web-unifiedporta-vue"



#�¼�Ŀ¼·��
assets = "\\src\\assets"
components = "\\src\\components"
icons = "\\src\\icons"
store = "\\src\\store"
styles = "\\src\\styles"
layout = "\\src\\views\\layout"

listMainPath = [sysconfigPath,messagePath,equipPath,personalPath,safetyPath,visitorPath,accountPath,unifiedportaPath ]
listSubPath = [assets,components,icons,store,styles,layout]

srcPath = vehiclePath
for mainPath in listMainPath:
    for subPath in listSubPath:
        path1 = srcPath + subPath
        path2 = mainPath +subPath
        os.system("xcopy %s %s /s /Y" % (path1, path2))









