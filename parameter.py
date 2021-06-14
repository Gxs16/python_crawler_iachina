'''
@Auth: Xinsheng.guo
@Date: 2021-6-12
'''
executable_path = r"D:\Guo_XS\crawlers\EdgeDriver\msedgedriver.exe"

target_url = "http://tiaokuan.iachina.cn:8090/sinopipi/loginServlet/publicQuery.do"

file_save_path = "./data/"

option_list = [('ProdTypeCode_00', '_00', '', ''),
                ('ProdTypeCode_00', '_01', '', ''),
                ('ProdTypeCode_00', '_02', '', ''),
                ('ProdTypeCode_01', '_00', '', ''),
                ('ProdTypeCode_01', '_01', '', ''),
                ('ProdTypeCode_02', '_00', '', ''),
                ('ProdTypeCode_02', '_01', '_00', '_00'),
                ('ProdTypeCode_02', '_01', '_00', '_01'),
                ('ProdTypeCode_02', '_01', '_00', '_02'),
                ('ProdTypeCode_02', '_01', '_01', '_00'),
                ('ProdTypeCode_02', '_01', '_01', '_01'),
                
                ('ProdTypeCode_02', '_01', '_02', ''),
                ('ProdTypeCode_02', '_01', '_03', ''),
                ('ProdTypeCode_02', '_01', '_04', ''),

                ('ProdTypeCode_03', '', '', ''),
                ('ProdTypeCode_04', '_00', '', ''),
                ('ProdTypeCode_04', '_01', '', ''),
                ]
