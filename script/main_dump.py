import json

import tool

data = {}

# --

i = 0
pp = tool.People()
pp["name"]["chi"] = "詹魁元"
pp["name"]["eng"] = "Kuei-Yuan Chan"
pp["year"] = 7
pp["alumni"] = False
pp["lab_id"] = "實驗室負責人 Director of SOLab"
pp["degrees"][0] = {"chi": "國立清華大學 學士", "eng": "B.S., National Tsing Hua University (97)"}
pp["degrees"][1] = {"chi": "美國密西根大學機械工程 博士", "eng": "Ph.D., University of Michigan (05)"}
pp["jobs"][0] = {"chi": "機械工程學系教授", "eng": "Professor of Mechanical Engineering", "web": None}
pp["jobs"][1] = {"chi": "台大創新設計學院教學組長", "eng": "Director of Academic Affairs, D-School@NTU", "web": None}
pp["jobs"][2] = {"chi": "台大副教務長", "eng": "Deputy Vice President for Academic Affairs", "web": None}
pp["show_paper"] = False
pp["papers"][0] = {
    "ref": """K.-Y. Chan, "Sequential Linearization in Analytical Target Cascading for Optimization of Complex Multilevel Systems", Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science, 225(2), pp.451-462, 2011""",
    "file": "",
    "drive": "",
    "type": "j",
    "year": 2011}
pp["papers"][1] = {
    "ref": """K.-Y. Chan, S. J. Skerlos, and P. Y. Papalambros, "A Method for Reliability-Based Optimization with Multiple Non-Normal Stochastic Parameters : A Simplified Airshed Management Case Study", Stochastic Environmental Research and Risk Assessment, 24(1), pp.101-116, 2010""",
    "file": "",
    "drive": "",
    "type": "j",
    "year": 2010}
pp["papers"][2] = {
    "ref": """K.-Y. Chan, M. Kokkolaras, P. Y. Papalambros, S. J. Skerlos and Z. Mourelatoes, "Propagation of Uncertainty in Optimal Design of Multilevel Systems: Piston-Ring/Cylinder-Liner Case Study," SAE Technical Paper 2004-01-1559, 2004""",
    "type": "ic",
    "file": "",
    "drive": "",
    "year": 2004}
pp["papers"][3] = {
    "ref": """K.-Y. Chan, S. J. Skerlos and P. Y. Papalambros, "Monotonicity and Active Set Strategies in Probabilistic Design Optimization", Journal of Mechanical Design, 128(4), 893-900, Jan 05, 2006""",
    "type": "j",
    "file": "",
    "drive": "",
    "year": 2006}
pp["papers"][4] = {
    "ref": """K.-Y. Chan, S. J. Skerlos and P. Y. Papalambros, "An Adaptive Sequential Linear Programming Algorithm for Optimal Design Problems With Probabilistic Constraints", Journal of Mechanical Design, 129(2), 140-149, Jan 23, 2006""",
    "type": "j",
    "file": "",
    "drive": "",
    "year": 2007}
pp["papers"][4] = {
    "ref": """K.-S. Lin, K.-Y. Chan and J.-J. Lee, "Kinematic error analysis and tolerance allocation of cycloidal gear reducers", Mechanism and Machine Theory, Vol. 124, Pages 73-91, June 2018""",
    "type": "j",
    "file": "2018KinematicErrorGearReducers_MMT.pdf",
    "drive": "https://drive.google.com/file/d/1YXhjruf6mCqc0neUL5dBS3W6S38um_ki/view?usp=sharing",
    "year": 2018}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "余岱璟"
pp["name"]["eng"] = "Dai-Jing Yu"
pp["year"] = 8
pp["degrees"][0] = {"chi": "元智大學 學士", "eng": "B.S., Yuan Ze University (05)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "National Cheng Kung University (08)"}
pp["jobs"][0] = {
    "chi": "德賽自動化技術有限公司", 
    "eng": "Huizhou Desay Automation Technology Co., LTD", 
    "web": "http://auto.desay.com/"}
pp["thesis"] = {
    "chi": "多目標最佳化之解集合在不確定因素下之分析及預測", 
    "eng": "Analysis and Prediction of the Shifts of Pareto Sets for Multi-Objective Optimization under Uncertainty", 
    "file": "YuDaiJung.pdf", 
    "drive": "https://drive.google.com/file/d/170VnY9eARaFx4iB4UFgpg8d209reUYM-/view?usp=sharing"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "劉智豪"
pp["name"]["eng"] = "Chih-Hao Liu"
pp["year"] = 8
pp["degrees"][0] = {"chi": "國立交通大學 學士", "eng": "B.S., National Chiao Tung University (03)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (08)"}
pp["jobs"][0] = {"chi": "瑞士商弗克司股份有限公司", 
    "eng": "Fox Factory Switzerland GmbH", 
    "web": "http://www.ridefox.com/"}
pp["thesis"] = {
    "chi": "壓力瓶在不確定因素下之構型最佳化設計", 
    "eng": "Reliability-Based Shape Optimization of a Pressure Tank under Random and Stochastic Environments", 
    "file": "LiuChihHao.pdf", 
    "drive": "https://drive.google.com/open?id=18WeMFU4-H6nHpx__kqc3dAns1OGJGuST"}
pp["papers"][0] = {
    "ref": """C.-H. Liu and K.-Y. Chan, "Reliability-Based Shape Optimization Of A Pressure Tank Under Random And Stochastic Environments", Proceedings of the ASME 2008 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, IDETC/CIE 2008, August 3-6, 2008, Brooklyn, New York, USA""",
    "file": "2008PressureTank_DETC.pdf",
    "drive": "https://drive.google.com/open?id=12SVKWL5R1wcriPq0i94lhsvrHKJQmMj_",
    "type": "ic",
    "year": 2008}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "何淳民"
pp["name"]["eng"] = "Chun-Min Ho"
pp["year"] = 8
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (08)"}
pp["degrees"][1] = {"chi": "美國密西根大學 碩士", "eng": "M.S., The University of Michigan (12)"}
pp["jobs"][0] = {
    "chi": "馬牌輪胎", 
    "eng": "Continental Tire of North America, LLC", 
    "web": "http://www.continentaltire.com/"}
pp["research"] = {
    "chi": "", 
    "eng": "Equality Constraints in Probabilistic Optimization Problems"}
pp["papers"][0] = {
    "ref": """C.-M. Ho and K.-Y. Chan, "Modified Reduced Gradient With Realizations Sorting for Hard Equality Constraints in Reliability-Based Design Optimization", ASME Journal of Mechanical Design, 133(1), 011004, 2011""",
    "file": "2011Equality_JMD.pdf",
    "drive": "https://drive.google.com/open?id=1_QvICkr6r80LyJh0G81rpzHcw1QD-A9V",
    "type": "j",
    "year": 2011}
pp["papers"][1] = {
    "ref": """D.-S. Lin, C.-M. Ho, and K.-Y. Chan, "Beta-Pareto Set Approximation for Multiobjective Optimization Under Uncertainty", Journal of Mechanical Design, 133(8), 081003, 2011""",
    "file": "2011BetaPareto_JMD.pdf",
    "drive": "https://drive.google.com/open?id=18dQhWqEU-KqS5sm-pXeZXti2r5eEV4OS",
    "type": "j",
    "year": 2011}
pp["papers"][2] = {
    "ref": """C.-M. Ho and K.-Y. Chan, "Modified Reduced Gradient with Realizations Sorting for Hard Equality Constraints in Reliability-Based Design Optimization", Proceedings of the ASME 2010 International Design Engineering Technical Conferences, Montreal, QC, Canada, August 15-18, 2010""",
    "file": "2010IDETC_Equality.pdf",
    "drive": "https://drive.google.com/open?id=1LnFDwcznNNqBNCZkqKJUfHHg7uPx6W4U",
    "type": "ic",
    "year": 2010}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "葉俊余"
pp["name"]["eng"] = "Jiun-Yu Yeh"
pp["year"] = 8
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (08)"}
pp["jobs"][0] = {
    "chi": "勁勝科技有限公司",
    "eng": "Jing Sheng Technology Co., LTD",
    "web": "http://www.jhing-sheng.com.tw/"}
pp["research"] = {
    "chi": "",
    "eng": "Design of Experiment of a Bio-Inspired Flapping Mechanism"
    }

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "林東信"
pp["name"]["eng"] = "Dong-Shin Lin"
pp["year"] = 9
pp["degrees"][0] = {"chi": "國立清華大學 學士", "eng": "B.S., National Tsing Hua University (07)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (09)"}
pp["jobs"][0] = {
    "chi": "美商史丹利七和國際股份有限公司", 
    "eng": "The Stanley Works", 
    "web": "http://stanley.stanleyblackanddecker.com.tw/"}
pp["thesis"] = {
    "chi": "以 β-Pareto 預測法解決不確定因素下之多目標最佳化", 
    "eng": "A Method to Predict β-Pareto Frontiers for Multiobjective Optimization under Uncertainty", 
    "file": "LinDongShin.pdf", 
    "drive": "https://drive.google.com/open?id=1us2mY5qJBk1ppEfMXPupw4JCmXGmzQsq"}
pp["papers"][0] = {
    "ref": """D.-S. Lin, C.-M. Ho, and K.-Y. Chan, "Beta-Pareto Set Approximation for Multiobjective Optimization Under Uncertainty", Journal of Mechanical Design, 133(8), 081003, 2011""",
    "file": "2011BetaPareto_JMD.pdf",
    "drive": "https://drive.google.com/open?id=18dQhWqEU-KqS5sm-pXeZXti2r5eEV4OS",
    "type": "j",
    "year": 2011}
pp["papers"][1] = {
    "ref": """K.-Y. Chan and D.-S. Lin, "Algorithm Developments for Optimization Problems with Joint Reliability Constraints", International Journal for Numerical Method in Engineering, 85(6), pp.768-783, 2011""",
    "file": "2011NME_JointConst.pdf",
    "drive": "https://drive.google.com/open?id=1Sr-bPVHN6zHOXdKaPCyHmYnaLq1dy_4Z",
    "type": "j",
    "year": 2011}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "許凱勛"
pp["name"]["eng"] = "Kai-Hsun Hsu"
pp["year"] = 9
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (07)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (09)"}
pp["jobs"][0] = {
    "chi": "台灣積體電路製造股份有限公司", 
    "eng": "Taiwan Semiconductor Manufacturing Company (TSMC)", 
    "web": "http://www.tsmc.com.tw/chinese/default.htm"}
pp["thesis"] = {
    "chi": "隨機取樣 SQP 演算法以解決非線性可靠度限制式之最佳化問題", 
    "eng": "A Filter-Based Sample Average SQP for Optimization Problems with Highly Nonlinear Probabilistic Constraints", 
    "file": "HsuKaiHsun.pdf", 
    "drive": "https://drive.google.com/open?id=1xFUdSoXCd_DuM9Evv35lZl9fTMQT4EHl"}
pp["papers"][0] = {
    "ref": """K.-S. Hsu and K.-Y. Chan, "A Filter-Based Sample Average SQP for Optimization Problems with Highly Nonlinear Probabilistic Constraints", Journal of Mechanical Design 132 (11), 111002, 2010""",
    "file": "2010SQPSampling_JMD.pdf",
    "drive": "https://drive.google.com/open?id=13uggsTzCSTf4yC94QCUlFuG37roUS-vT",
    "type": "j",
    "year": 2010}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "吳昱達"
pp["name"]["eng"] = "Yu-Ta Wu"
pp["year"] = 10
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (08)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (10)"}
pp["jobs"][0] = {
    "chi": "國立台灣大學創新設計學院", 
    "eng": "D-School, National Taiwan University", 
    "web": "http://dschool.ntu.edu.tw/"}
pp["thesis"] = {
    "chi": "可靠度最佳化方法應用於不確定因素下之城市交通法規制定", 
    "eng": "Extension of Probabilistic Optimization to UrbanTraffic Policy-Setting Under Uncertainty", 
    "file": "WuYuTa.pdf", 
    "drive": "https://drive.google.com/open?id=1jDiz31nnpqRnOXwxQZq31SCqorUWMPtW"}
pp["papers"][0] = {
    "ref": """Y.-T. Wu and K.-Y. Chan, "Optimal Design and Impact Analysis of Urban Traffic Regulations Under Ambient Uncertainty", Stochastic Environmental Research and Risk Assessment, 25(2), P.271-286, 2011""",
    "file": "2011TrafficCA_SERRA.pdf",
    "drive": "https://drive.google.com/open?id=1oHgMNYlvDfcaAE2n3Xel3jv8fxCZgo_h",
    "type": "j",
    "year": 2011}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "張琇雯"
pp["name"]["eng"] = "Hsiu-Wen Chang"
pp["year"] = 10
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (08)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (10)"}
pp["jobs"][0] = {
    "chi": "華創車電技術中心股份有限公司", 
    "eng": "Hua-Chuang Automobile Information Technical Center Co., Ltd.", 
    "web": "http://www.haitec.com.tw/tc/"}
pp["thesis"] = {
    "chi": "移動式汙染源於不確定因素下制訂法規與測站點之循序最佳化方法", 
    "eng": "Sequential Optimization of Transportation Regulations and Receptor Locations for Urban Mobile Emissions Under Uncertainty", 
    "file": "ChangHsiuWen.pdf", 
    "drive": "https://drive.google.com/open?id=1BbrgBOYv5KV8zylss4jl6_pZLcYE_2-M"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "洪子頡"
pp["name"]["eng"] = "Tzu-Chieh Hung"
pp["year"] = 10
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (08)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (10)"}
pp["degrees"][2] = {"chi": "國立台灣大學 博士", "eng": "Ph.D., National Taiwan University (16)"}
pp["jobs"][0] = {
    "chi": "宏碁股份有限公司", 
    "eng": "Acer Incorporated", 
    "web": "https://www.acer.com/ac/zh/TW/content/home"}
pp["thesis"] = {
    "chi": "不確定因素下整合風能微電網系統之設備規劃與配電策略最佳化", 
    "eng": "Optimization of A Wind-Integrated Microgrid System with Equipment Sizing and Dispatch Strategy", 
    "file": "TzuChiehHung.pdf", 
    "drive": "https://drive.google.com/open?id=1hLzPLXtLL_fsoGHFw5LaJqVGUjod5nmc"}
pp["papers"][0] = {
    "ref": """T.-C. Hung and K.-Y. Chan, "Multi-Objective Design and Tolerance Allocation for Single- and Multi-Level Systems", Journal of Intelligent Manufacturing, 24(3), pp.559-573, 2013""",
    "file": "2013ToleranceAllocation_JIMS.pdf",
    "drive": "https://drive.google.com/open?id=1oYkQAJZwZe3IRrNc1V20FO0BNVgveu8x",
    "type": "j",
    "year": 2013}
pp["papers"][1] = {
    "ref": """T.-C. Hung and K.-Y. Chan, "Uncertainty Quantification of Pareto Optima in Multiobjective Problems", Journal of Intelligent Manufacturing, 24(2), pp.385-395, 2013""",
    "file": "2013ParetoQuantification_JIMS.pdf",
    "drive": "https://drive.google.com/open?id=15Tjb6TVGWkw9tzCpwyuD4VdGxapr8vlm",
    "type": "j",
    "year": 2013}
pp["papers"][2] = {
    "ref": """T.-C. Hung and K.-Y. Chan, "Uncertainty Quantifications of Pareto Optima in Multiobjective Problems", the 9th World Congress on Structural and Multidisciplinary Optimization, Shizuoka, Japan, June 13-17, 2011""",
    "file": "2011WCSMO9_OIR.pdf",
    "drive": "https://drive.google.com/open?id=1SN8_9fjBoi6qv8JKeI7EsxqcOwyqb-Xm",
    "type": "ic",
    "year": 2011}
pp["papers"][3] = {
    "ref": """T.-C. Hung and K.-Y. Chan, "Multi-Objective Design and Tolerance Allocation for Single- and Multi-Level Systems", Proceedings of the ASME 2010 International Design Engineering Technical Conferences, Montreal, QC, Canada, August 15-18, 2010""",
    "file": "2010IDETC_ToleranceAllocation.pdf",
    "drive": "https://drive.google.com/open?id=1jPY2Gil_TM2Ls-xrh4EApWJRBMZsIS2a",
    "type": "ic",
    "year": 2010}
pp["papers"][4] = {
    "ref": """T.-C. Hung and K.-Y. Chan, "Probability-based Power Dispatch in Wind-Integrated Electrical Grid for Energy Storage Capacity Determination", Proceedings of the ASME International Design Engineering Technical Conferences & Computer and Information in Engineering Conference, Charlotte, NC, USA, 2016""",
    "file": "2016WindElectricalEnergy_ASME.pdf",
    "drive": "https://drive.google.com/open?id=1AKfxFruoFRfemdEETS2DHJ2oDa45qm3G",
    "type": "ic",
    "year": 2016}
pp["papers"][5] = {
    "ref": """T.-C. Hung and K.-Y. Chan, "Optimization of a Wind-Integrated Microgrid System with Equipment Sizing and Dispatch Strategy under Resource Uncertainty", Journal of Mechanical Design, 137(4), 041403, Apr. 01, 2015""",
    "file": "2015Microgrid_JMD.pdf",
    "drive": "https://drive.google.com/open?id=1IiTtTVs7pHdjG11wHjwfeP2FgWcCTeyD",
    "type": "j",
    "year": 2015}
pp["papers"][6] = {
    "ref": """T.-C. Hung and K.-Y. Chan, "Component Size Optimization of a Wind-Integrated Microgram System with Dispatch Strategy and Resource Uncertainty", Proceedings of the 2014 International Design Engineering Technical Conferences, Buffalo, NY, USA, August 17-20, 2014""",
    "file": "2014IDETC_hungtc.pdf",
    "drive": "https://drive.google.com/open?id=1h6YLL8pdfKpigy4omDsPs22VfiIoX22w",
    "type": "ic",
    "year": 2014}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "劉季儒"
pp["name"]["eng"] = "Chi-Ju Liu"
pp["year"] = 11
pp["degrees"][0] = {"chi": "國立交通大學 學士", "eng": "B.S., National Chiao Tung University (09)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (11)"}
pp["jobs"][0] = {
    "chi": "將群智權集團", 
    "eng": "JC IP Group", 
    "web": "http://www.jcipgroup.com/"}
pp["thesis"] = {
    "chi": "時變可靠度最佳化演算法：PHI2 與 MADS 之整合", 
    "eng": "Integration of PHI2 Method with MADS for Optimization with Time-Variant Reliability Constraints", 
    "file": "LiuChiJu.pdf", 
    "drive": "https://drive.google.com/open?id=1RahQXEy0LZXwCTVjWIKUWs6m9qEMony0"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "許佳豪"
pp["name"]["eng"] = "Chiao-Hao Hsu"
pp["year"] = 11
pp["degrees"][0] = {"chi": "國立雲林科技大學 學士", "eng": "B.S., National Yunlin University of Science and Technology (09)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (11)"}
pp["jobs"][0] = {
    "chi": "台灣積體電路製造股份有限公司", 
    "eng": "Taiwan Semiconductor Manufacturing Company (TSMC)", 
    "web": "http://www.tsmc.com.tw/chinese/default.htm"}
pp["thesis"] = {
    "chi": "可靠度設限資料之反應曲面於工程設計演進之應用", 
    "eng": "Surrogate-Assisted Design Evolution with Censored Reliability Data in Engineering Design", 
    "file": "HsuChiaHao.pdf", 
    "drive": "https://drive.google.com/open?id=1u49eNSca4oYBfZc_GHXuKxHdbUfLfmx5"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "張勝昌"
pp["name"]["eng"] = "Sheng-Chang Chang"
pp["year"] = 11
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (09)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (11)"}
pp["jobs"][0] = {
    "chi": "華創車電技術中心股份有限公司", 
    "eng": "Hua-Chuang Automobile Information Technical Center Co., Ltd.", 
    "web": "http://www.haitec.com.tw/tc/"}
pp["thesis"] = {
    "chi": "複雜工程系統的循序暫緩設計方法", 
    "eng": "Iterative Suspension and Solution Strategy for Complex Multidisciplinary Engineering Design", 
    "file": "ChangShenChang.pdf", 
    "drive": "https://drive.google.com/open?id=1pn0nsgK8s7nHnpTs-9XU-8AevJzY8i6U"}
pp["papers"][0] = {
    "ref": """S.-C. Chang and K.-Y. Chan, "Iterative Decomposition and Solution Strategy for Complex Engineering Problems", the 9th World Congress on Structural and Multidisciplinary Optimization, Shizuoka, Japan, June 13-17, 2011""",
    "file": "2011WCSMO9_ATCSuspend.pdf",
    "drive": "https://drive.google.com/open?id=1xGVfZwnNwvxqo9khEqyojI-9y1HRxAN7",
    "type": "ic",
    "year": 2011}
pp["papers"][1] = {
    "ref": """S.-C. Chang and K.-Y. Chan, "Multidisciplinary Design of Vehicle Silhouettes Considering Engineering and Aesthetics Measures", (Best Paper Award) International Conference on Innovative Design and Manufacturing, December 12-14, 2012""",
    "file": "",
    "drive": "",
    "type": "ic",
    "year": 2012}
pp["papers"][2] = {
    "ref": """K.-Y. Chan and S.-C. Chang, "A Preliminary Study on the Integration of Engineering and Aesthetics Measures via the Design of Vehicle Silhouettes", Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science, Volume: 229 issue: 12, pp. 2221-2230, August 1, 2015""",
    "file": "2014JMES_Aesthetics.pdf",
    "drive": "https://drive.google.com/open?id=12uhsCjcQLbH-hpfR_dSeNwuj5REEQq9U",
    "type": "j",
    "year": 2015}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "郭祐伸"
pp["name"]["eng"] = "Yu-Shen Kuo"
pp["year"] = 11
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (10)"}
pp["jobs"][0] = {
    "chi": "廣達電腦股份有限公司", 
    "eng": "Quanta Computer Incorporated", 
    "web": "http://www.quantatw.com/Quanta/chinese/Default.aspx"}
pp["research"] = {
    "chi": "", 
    "eng": "Scenario Analyses of Traffic Regulations using Nagel-Schreckenberg Model"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "吳嘉珮"
pp["name"]["eng"] = "Chia-Pei Wu"
pp["year"] = 11
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (10)"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "陳力豪"
pp["name"]["eng"] = "Li-Hao Chen"
pp["year"] = 12
pp["degrees"][0] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (12)"}
pp["jobs"][0] = {
    "chi": "友達光電股份有限公司", 
    "eng": "AU Optronics Corporation", 
    "web": "https://auo.com/zh-TW"}
pp["thesis"] = {
    "chi": "風力發電場規劃與發電機葉片設計在地理限制下之整合研究", 
    "eng": "Wind Farm Optimization with Turbine Blade Design Considering Geographical Constraints", 
    "file": "ChenLiHao", 
    "drive": "https://drive.google.com/open?id=1cQu1tizFqkFWF8hwFbtiW92j5Nj4eBTr"}
pp["papers"][0] = {
    "ref": """L.-H. Chen and K.-Y. Chan, "風力發電廠規劃與發電機葉片設計在地理限制下之整合研究", the 29st Chinese Society of Mechanical Engineers Conference, Dec., 2012""",
    "type": "dc",
    "file": "",
    "drive": "",
    "year": 2012}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "林彬儀"
pp["name"]["eng"] = "Pin-Yi Lin"
pp["year"] = 12
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (10)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (13)"}
pp["jobs"][0] = {
    "chi": "東元電機股份有限公司", 
    "eng": "TECO Electric and Machinery Co., Ltd.", 
    "web": "http://www.teco.com.tw/"}
pp["thesis"] = {
    "chi": "針對非充裕不確定資料設計之最佳取樣與資源配置", 
    "eng": "Optimal Sample Augmentation and Resource Allocation for Design with Inadequate Uncertainty Data", 
    "file": "LinPinYi.pdf", 
    "drive": "https://drive.google.com/open?id=180PXCnUFZD-ps3IaKAF1I66OpHsY3xoC"}
pp["papers"][0] = {
    "ref": """P.-Y. Lin and K.-Y. Chan, "Optimal Sample Augmentation and Resource Allocation for Design with Inadequate Uncertainty Data ", Proceedings of the ASME International Design Engineering Technical Conference, Montreal, Canada, August 12-15, 2012""",
    "file": "",
    "drive": "",
    "type": "ic",
    "year": 2012}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "薛伊倩"
pp["name"]["eng"] = "Yi-Chien Hsueh"
pp["year"] = 12
pp["degrees"][0] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (12)"}
pp["jobs"][0] = {
    "chi": "華創車電技術中心股份有限公司", 
    "eng": "Hua-Chuang Automobile Information Technical Center Co., Ltd.", 
    "web": "http://www.haitec.com.tw/tc/"}
pp["thesis"] = {
    "chi": "公差與剛性對機械手臂於承載下精度之影響", 
    "eng": "Impact of Tolerance and Stiffness on the Accuracy of Manipulators with Payload", 
    "file": "HsuehYiChien.pdf", 
    "drive": "https://drive.google.com/open?id=1oLV5mWTnMSrPKuJ8hu-SKhs-1YccEcMu"}
pp["papers"][0] = {
    "ref": """K.-L. Li, M.-C. Lai, Y.-C. Hsueh and K.-Y Chan, "Analysis of Uncertainties in Planar Robot Manipulation", the 31st Chinese Society of Mechanical Engineers Conference, Taichung, Taiwan, 2014""",
    "file": "2014CSME_AURM2D.pdf",
    "drive": "https://drive.google.com/open?id=1mq_NoiO-_Us1w6PyJ1qjnocEc8FiZOnV",
    "type": "ic",
    "year": 2014}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "王宏偉"
pp["name"]["eng"] = "Hong-Wei Wang"
pp["year"] = 12
pp["degrees"][0] = {"chi": "國立成功大學 交換生", "eng": "Undergraduate Visiting Student, National Cheng Kung University (12)"}
pp["research"] = {
    "chi": "", 
    "eng": "GearTrain System Design and Analysis"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "韓佾君"
pp["name"]["eng"] = "Yi-Chun Han"
pp["year"] = 13
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (11)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (13)"}
pp["jobs"][0] = {
    "chi": "泰金寶電通股份有限公司", 
    "eng": "Cal-Comp Electronics & Communications Co., Ltd", 
    "web": "http://www.newkinpogroup.com/big5/"}
pp["thesis"] = {
    "chi": "貝氏更新法應用於皮帶系統與不確定性壽命資料之設計整合", 
    "eng": "A Bayesian Based Updating Scheme for Belt-Pulley Systems Design with Censored Life Data", 
    "file": "HanYiChun.pdf", 
    "drive": "https://drive.google.com/open?id=1a2fKTyx1whggoMqqYs1xegIUO_GAgZmD"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "米約瑟"
pp["name"]["eng"] = "Joseph Millogo"
pp["year"] = 13
pp["alumni"] = False
pp["lab_id"] = "博士候選人 Ph.D. Candidate"
pp["degrees"][0] = {"chi": "土耳其東地中海大學 學士", "eng": "B.S., Eastern Mediterranean University (08)"}
pp["degrees"][1] = {"chi": "昆山科技大學 碩士", "eng": "M.S., Kun Shan University (11)"}
pp["research"] = {
    "chi": "", 
    "eng": "Modified Principle Component Analysis for Time Varying Data Mining with Uncertainties"}
pp["papers"][0] = {
    "ref": """J. Millogo and K.-Y. Chan, "Life Cycle Assessment under Uncertainty - a review", the Asia Design Engineering Workshop, Taipei, Taiwan, November 20-22, 2014""",
    "file": "2014ADEWS_LCAReview",
    "drive": "https://drive.google.com/open?id=10pFPL8mz5LuUfRWxuqK7Y1_ycPqB-m6B",
    "type": "ic",
    "year": 2014}
pp["papers"][1] = {
    "ref": """J. Millogo and K.-Y. Chan, "Multivariate Analysis of Extrapolating Time-Invariant Data with Uncertainty", International Journal for Uncertainty Quantification, (Accepted, 2019)""",
    "file": "",
    "drive": "",
    "type": "j",
    "year": 2019}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "吳典運"
pp["name"]["eng"] = "Dian-Yun Wu"
pp["year"] = 13
pp["degrees"][0] = {"chi": "國立臺灣海洋大學 學士", "eng": "B.S., National Taiwan Ocean University (10)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (13)"}
pp["jobs"][0] = {
    "chi": "華創車電技術中心股份有限公司", 
    "eng": "Hua-Chuang Automobile Information Technical Center Co., Ltd.", 
    "web": "http://www.haitec.com.tw/tc/"}
pp["thesis"] = {
    "chi": "因應資料不確定性之最佳複合式反應曲面", 
    "eng": "Composites of Surrogates with Data Uncertainty", 
    "file": "WuDianYun.pdf", 
    "drive": "https://drive.google.com/open?id=1jDiz31nnpqRnOXwxQZq31SCqorUWMPtW"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "王東泰"
pp["name"]["eng"] = "Dong-Tai Wang"
pp["year"] = 13
pp["degrees"][0] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (13)"}
pp["thesis"] = {
    "chi": "利用反應曲面輔助 DIRECT 演算法處理耗時工程設計問題", 
    "eng": "Surrogate-Assisted DIRECT Algorithm for Optimization Problems with Expensive Engineering Simulations", 
    "file": "WangDongTai.pdf", 
    "drive": "https://drive.google.com/open?id=1y4eWafky0SBvDNfcu9izHSvxE_pV7FhZ"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "陳煜駿"
pp["name"]["eng"] = "Yee-Chun Tan"
pp["year"] = 13
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (13)"}
pp["jobs"][0] = {
    "chi": "", 
    "eng": "Petrofac Malaysia", 
    "web": "https://www.petrofac.com/en-gb/home/"}
pp["research"] = {
    "chi": "", 
    "eng": "Design and Analysis of Vehicle Belt-driven Starter Generator"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "賴明證"
pp["name"]["eng"] = "Min-Cheng Lai"
pp["year"] = 14
pp["degrees"][0] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (14)"}
pp["jobs"][0] = {
    "chi": "鴻海科技集團", 
    "eng": "Foxconn Technology Group", 
    "web": "http://www.foxconn.com.tw/"}
pp["thesis"] = {
    "chi": "機器手臂在考量關節間隙下之多目標路徑規劃", 
    "eng": "Multi-objective Path Planning for Robot Manipulators with Joint Clearance", 
    "file": "LaiMinCheng.pdf", 
    "drive": "https://drive.google.com/open?id=1Y2sWLLN3LIuA0xfLlmubIbMW2vva7ZSw"}
pp["papers"][0] = {
    "ref": """M.-C. Lai and K.-Y. Chan, "Minimal Deviation Paths for Manipulators with Joint Clearances", Proceedings of the 2014 International Design Engineering Technical Conferences, Buffalo, NY, USA, August 17-20, 2014""",
    "file": "2014IDETC_laimc.pdf",
    "drive": "https://drive.google.com/open?id=1HMJfmiov0sQyuIggibSy1W7FspMAJmpO",
    "type": "ic",
    "year": 2014}
pp["papers"][1] = {
    "ref": """K.-L. Li, M.-C. Lai, Y.-C. Hsueh and K.-Y Chan, "Analysis of Uncertainties in Planar Robot Manipulation", the 31st Chinese Society of Mechanical Engineers Conference, Taichung, Taiwan, 2014""",
    "file": "2014CSME_AURM2D.pdf",
    "drive": "https://drive.google.com/open?id=1mq_NoiO-_Us1w6PyJ1qjnocEc8FiZOnV",
    "type": "ic",
    "year": 2014}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "蘇庭玉"
pp["name"]["eng"] = "Dale Su"
pp["year"] = 14
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (12)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (14)"}
pp["jobs"][0] = {
    "chi": "愛爾蘭商速聯股份有限公司", 
    "eng": "SRAM Corporation", 
    "web": "https://www.sram.com/"}
pp["thesis"] = {
    "chi": "人機系統中人為誤差補償方法", 
    "eng": "Compensating For Operational Uncertainty in Man-Machine System: A case Study On Intelligent Vehicle Parking Assist", 
    "file": "SuDale.pdf", 
    "drive": "https://drive.google.com/open?id=1h0j4ZwE9-A_vo84hVN0e4R1J6LZ7pqnA"}
pp["papers"][0] = {
    "ref": """D. Su and K.-Y. Chan, "Compensating for Operational Uncertainty in Man-Machine Systems - a case study on intelligent vehicle parking assist", Proceedings of the ASME 2014 International Design and Engineering Technical Conference and Computers and Information in Engineering Conference, Buffalo, New York, USA, Aug 17-20, 2014""",
    "file": "2014IDETC2014_sudale_draft",
    "drive": "https://drive.google.com/open?id=1BUFrGVE2OXW1_661cO9c_qVNK_DQQHDN",
    "type": "ic",
    "year": 2014}
pp["papers"][1] = {
    "ref": """D. Su and K.-Y. Chan, "Compensating for Operational Uncertainty in Man-Machine Systems : A Case Study on Intelligent Vehicle Parking Assist System", ASCE-ASME Journal of Risk and Uncertainty in Engineering Systems : Part B. Mechanical Engineering, 2015""",
    "file": "2015JRISK_ManMachine.pdf",
    "drive": "https://drive.google.com/open?id=1pnW3pRsSte6Kuve5QpscSDCAJj5H4DOa",
    "type": "j",
    "year": 2015}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "顏肇余"
pp["name"]["eng"] = "Chao-Yu Yen"
pp["year"] = 14
pp["degrees"][0] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (14)"}
pp["jobs"][0] = {
    "chi": "泰金寶電通股份有限公司", 
    "eng": "Cal-Comp Electronics & Communications Co., Ltd", 
    "web": "http://www.newkinpogroup.com/big5/"}
pp["thesis"] = {
    "chi": "結合重要性指標與敏感度以提升連鎖失效系統之可靠度", 
    "eng": "Integrating Importance Measure with Sensitivity Analysis to Improve the Reliability of Cascading Failure System", 
    "file": "YenChaoYu.pdf", 
    "drive": "https://drive.google.com/open?id=16sOiHehxvbhwUj9LzBVcBquO8EA0nJFg"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "張值榕"
pp["name"]["eng"] = "Chih-Jung Chang"
pp["year"] = 14
pp["degrees"][0] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (14)"}
pp["jobs"][0] = {
    "chi": "鴻海科技集團", 
    "eng": "Foxconn Technology Group", 
    "web": "http://www.foxconn.com.tw/"}
pp["thesis"] = {
    "chi": "不確定因素下異構風場的多目標分析", 
    "eng": "Multi-criteria Analysis of Heterogeneous Wind Farms under Uncertainty", 
    "file": "ChangChihJung.pdf", 
    "drive": "https://drive.google.com/open?id=1e74x5eeLSNq2643eUPlBUzirpH_qGT3S"}
pp["papers"][0] = {
    "ref": """C.-J. Chang, P.-S. Lin, and K.-Y. Chan, "The Concept of Heterogeneity in Wind Farm Optimization", the Asia Design Engineering Workshop, Taipei, Taiwan, November 20-22, 2014""",
    "file": "2014WindFarm_DEWS",
    "drive": "https://drive.google.com/open?id=1DqbdyjKzmSBaGoOPU_BAB9Uv_h1tHbhg",
    "type": "ic",
    "year": 2014}
pp["papers"][1] = {
    "ref": """C.-J. Chang and K.-Y. Chan, "Bi-objective Wind Farm Optimization with Turbine Blade Design under Uncertainty", International Engineering Optimization Conference, Lisbon, Portugal, 2014""",
    "file": "",
    "drive": "",
    "type": "ic",
    "year": 2014}
    
pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "林佑安"
pp["name"]["eng"] = "You-An Lin"
pp["year"] = 15
pp["degrees"][0] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (15)"}
pp["jobs"][0] = {
    "chi": "漢翔航空工業股份有限公司", 
    "eng": "Aerospace Industrial Development Corporation", 
    "web": "http://www.aidc.com.tw/tw/"}
pp["thesis"] = {
    "chi": "車流模擬與車輛設計於都會區機車油耗減量之整合", 
    "eng": "Reducing the Fuel Consumption of Urban Scooter Fleet via Integrating Traffic Simulation in Vehicle Design", 
    "file": "LinYouAn.pdf", 
    "drive": "https://drive.google.com/open?id=1N9PvtFqLt2lWo1C0-NPMFoCOf0gTSxsz"}
pp["papers"][0] = {
    "ref": """Y.-A. Lin and K.-Y. Chan, "A Direct Simulation Method for Continuous Variable Transmission with Component-wise Design Specifications", the 17st Chinese Society of Mechanism and Machine Theory Conference, Taichung, Taiwan, Nov. 14, 2014""",
    "file": "",
    "drive": "",
    "type": "dc",
    "year": 2014}
pp["papers"][1] = {
    "ref": """Y.-A. Lin, P.-A. Chen and K.-Y. Chan, "A Method for Reducing Fuel Consumption of Urban Scooters Using Vehicle Design and Traffic Simulation", Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science, Vol. 231, issue 7, pp.1252-1271, April 1, 2017""",
    "file": "2016ReducingConsumptionVehicleTraffic_SAGE.pdf",
    "drive": "https://drive.google.com/open?id=1PQ7-6ozJZV3WsVfWu22Xr_XRzEZh1Zat",
    "type": "j",
    "year": 2016}
pp["papers"][2] = {
    "ref": """Y.-A. Lin and K.-Y. Chan, "Comparisons between Direct and Inverse Analysis Methods in Continuous Variable Transmissions with Comprehensive Component Specifications", the 31st Chinese Society of Mechanical Engineers Conference, Taichung, Taiwan, 2014""",
    "file": "2014CSME_CVTMethodsComparison.pdf",
    "drive": "https://drive.google.com/open?id=18gNTA86ydBqggI6UuVm6pKq6JZTP0XXM",
    "type": "dc",
    "year": 2014}
pp["papers"][3] = {
    "ref": """Y.-A. Lin and K.-Y. Chan, "A Direct Simulation Method for Continuous Variable Transmission with Component-wise Design Specifications", Mechanism and Mechanical Technology Conference, Taichung, Taiwan, 2014""",
    "file": "2014THCSMMT_CVTDirectSimulation.pdf",
    "drive": "https://drive.google.com/open?id=1Z3fnxiMEB6V-_b_tog2q22plpjX1alhl",
    "type": "ic",
    "year": 2014}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "張祐晨"
pp["name"]["eng"] = "You-Chen Chang"
pp["year"] = 15
pp["degrees"][0] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (15)"}
pp["jobs"][0] = {
    "chi": "建準電機工業股份有限公司", 
    "eng": "Sunonwealth Electric Machine Industry co., lt", 
    "web": "http://www.sunon.com.tw/"}
pp["thesis"] = {
    "chi": "用於提升電子系統可靠度之貝式失效診斷法", 
    "eng": "A Bayesian-Based Fault Diagnosis Method for Reliability Improvement of Electric System", 
    "file": "ChangYouChen.pdf", 
    "drive": "https://drive.google.com/open?id=1RDu8mAbWHuNPJtTlzy8XHVtVC0ECE9L_"}
pp["papers"][0] = {
    "ref": """Y.-C. Chang, H.-W. Huang, K.-Y. Chan, W.-F. Wu and T.-C. Liu, "Enhanced Markovian Model with Physics of Failures for Long-term Reliability Analysis of Electrical Systems", the 14th World Congress in Mechanism and Machine Science, Taipei, Taiwan, October 25-30, 2015""",
    "file": "2015IFToMM_ElectronicsReliability.pdf",
    "drive": "https://drive.google.com/open?id=1UFjQB6PD07p61CuouiAJt4IJnHwpdDAI",
    "type": "ic",
    "year": 2015}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "陳柏安"
pp["name"]["eng"] = "Pao-An Chen"
pp["year"] = 16
pp["degrees"][0] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (16)"}
pp["jobs"][0] = {
    "chi": "將群智權集團", 
    "eng": "JC IP Group", 
    "web": "http://www.jcipgroup.com/"}
pp["thesis"] = {
    "chi": "以混合車流模型為基礎之最佳路網避障路徑規劃", 
    "eng": "The Optimal Route Planning for Road Network with Obstacles using Mixed Fleets", 
    "file": "PaoAnChen.pdf", 
    "drive": "https://drive.google.com/open?id=1VQYagihZIT_zWvew3umSBxBp3vg8s0uF"}
pp["papers"][0] = {
    "ref": """P.-A. Chen and K.-Y. Chan, "A Novel Traffic Simulation with Mixed Flow for Obstacle Avoidance Analysis and Strategy", the 32nd Chinese Society of Mechanical Engineers Conference, Kaohsiung, Taiwan, December 11-12, 2015""",
    "file": "2015CSME_Traffic.pdf",
    "drive": "https://drive.google.com/open?id=1Od1a9XzeXD0u7bJ_eFlNElPTRxZPmOnF",
    "type": "ic",
    "year": 2015}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "李冠霖"
pp["name"]["eng"] = "Kuan-Lin Li"
pp["year"] = 16
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (14)"}
pp["degrees"][1] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (16)"}
pp["jobs"][0] = {
    "chi": "台達電子工業股份有限公司", 
    "eng": "Delta Electronics, Inc.", 
    "web": "http://www.deltaww.com/"}
pp["thesis"] = {
    "chi": "機械手臂之關節間隙評估與運行精度提升之方法", 
    "eng": "Analysis and Accuracy Improvement of Robot Manipulators with Joint Clearance", 
    "file": "KuanLinLi.pdf", 
    "drive": "https://drive.google.com/open?id=1m8XLDGgIIyljSsjk4bxAOdzoFrOh1NDP"}
pp["papers"][0] = {
    "ref": """K.-L. Li, M.-C. Lai, Y.-C. Hsueh and K.-Y Chan, "Analysis of Uncertainties in Planar Robot Manipulation", the 31st Chinese Society of Mechanical Engineers Conference, Taichung, Taiwan, 2014""",
    "file": "2014CSME_AURM2D.pdf",
    "drive": "https://drive.google.com/open?id=1mq_NoiO-_Us1w6PyJ1qjnocEc8FiZOnV",
    "type": "ic",
    "year": 2014}
pp["papers"][1] = {
    "ref": """K.-L. Li, W.-T. Yang, K.-Y. Chan and P.-C. Lin, "An Optimization Technique for Serial Manipulator Robots Parameter Calibration and Accuracy Improvement", the 32nd Chinese Society of Mechanical Engineers Conference, Kaohsiung, Taiwan, December 11-12, 2015""",
    "file": "2015CSME_RobotArm.pdf",
    "drive": "https://drive.google.com/open?id=191ccFyFupfsBL5UbCtyB1FeV1QlS4qZG",
    "type": "ic",
    "year": 2015}
pp["papers"][2] = {
    "ref": """K.-L. Li, W.-T. Yang, K.-Y. Chan and P.-C. Lin, "An Optimization Technique for Identifying Robot Manipulator Parameters Under Uncertainty", Springer Plus, 5:1771, 2016""",
    "file": "2016IdentifyParameters_Springerplus.pdf",
    "drive": "https://drive.google.com/open?id=1GD1iEPttI9TcR3A2hhX2dGUB-cwYzvr-",
    "type": "j",
    "year": 2016}
pp["papers"][3] = {
    "ref": """K.-L. Li, Y.-K. Tsai, and K.-Y. Chan, "Identifying Joint Clearance via Robot Manipulation", Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science 232, no. 15, August, 2018""",
    "file": "2017IdentifyingJointClearanceViaRobotManipulation.pdf",
    "drive": "https://drive.google.com/open?id=1SQ-gNonKEOLpVgICCrkjjzgYB8nFnYLB",
    "type": "j",
    "year": 2018}
pp["papers"][0] = {
    "ref": """K.-L. Li, M.-C. Lai, Y.-C. Hsueh and K.-Y Chan, "Analysis of Uncertainties in Planar Robot Manipulation", the 31st Chinese Society of Mechanical Engineers Conference, Taichung, Taiwan, 2014""",
    "file": "2014CSME_AURM2D.pdf",
    "drive": "https://drive.google.com/open?id=1mq_NoiO-_Us1w6PyJ1qjnocEc8FiZOnV",
    "type": "ic",
    "year": 2014}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "林柏伸"
pp["name"]["eng"] = "Po-Shen Lin"
pp["year"] = 16
pp["degrees"][0] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (16)"}
pp["thesis"] = {
    "chi": "考量葉片幾何形狀之風場設計自動化", 
    "eng": "Design Automation of Wind Farm Planning with Turbine Blade Geometry", 
    "file": "PoShenLin.pdf", 
    "drive": "https://drive.google.com/open?id=1c-kVdsDfJBxRAphrijrYuUg8OfwNq1bs"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "林岳羿"
pp["name"]["eng"] = "Yueh-I Lin"
pp["year"] = 16
pp["degrees"][0] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (16)"}
pp["jobs"][0] = {
    "chi": "台達電子工業股份有限公司", 
    "eng": "Delta Electronics, Inc.", 
    "web": "http://www.deltaww.com/"}
pp["thesis"] = {
    "chi": "使用模型校準以識別複雜系統參數數值之方法", 
    "eng": "Identifying Parameter Uncertainties in Model Calibration of Complex Systems", 
    "file": "YuehILin.pdf", 
    "drive": "https://drive.google.com/open?id=1P7bjDBSKUW8QXsOVuMZqEASKoFZsci0V"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "劉欣怡"
pp["name"]["eng"] = "Shin-Yi Low"
pp["year"] = 16
pp["degrees"][0] = {"chi": "國立台灣大學 學士", "eng": "B.S., National Taiwan University (14)"}
pp["degrees"][1] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (17)"}
pp["jobs"][0] = {
    "chi": "光寶科技股份有限公司", 
    "eng": "LITE-ON Technology Group", 
    "web": "https://www.liteon.com/zh-tw"}
pp["thesis"] = {
    "chi": "跆拳道踢擊的生物力學不確定因素", 
    "eng": "Uncertainty in the Biomechanics of Taekwondo Kick", 
    "file": "LowShinYi.pdf", 
    "drive": "https://drive.google.com/open?id=1dBAxdFs839G99lXTOFYu2m5ZFSwFV5Ry"}
pp["papers"][0] = {
    "ref": """S. Low and K.-Y. Chan, "Uncertainty in the Biomechanics of Taekwondo Kick", International Workshop on Reliability for Advanced Technology, Taipei, Taiwan, Feb 16, 2017""",
    "file": "",
    "drive": "",
    "type": "ic",
    "year": 2017}
pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "游右均"
pp["name"]["eng"] = "Yu-Chun Yu"
pp["year"] = 17
pp["degrees"][0] = {"chi": "國立台灣大學 學士", "eng": "B.S., National Taiwan University (15)"}
pp["degrees"][1] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (17)"}
pp["thesis"] = {
    "chi": "人與自動駕駛的不確定因素分析與可靠度比較應用於現有車輛上－變換車道案例分析", 
    "eng": "Uncertainty Analysis and Reliability Comparisons between Human and Computer Drivers for On-Road Vehicles : A Case on Lane-change", 
    "file": "YuYuChun.pdf", 
    "drive": "https://drive.google.com/open?id=1ea7-sWDjCF1KeNP8yw6dfbocWrJ6cOoJ"}
pp["papers"][0] = {
    "ref": """Y.-C. Yu and K.-Y. Chan, "A Study on the Lane-changing Intension and Detection for Autonomous Vehicles", the 21st National Conference on Vehicle Engineering, Tainan, Taiwan, Nov 18, 2016""",
    "type": "dc",
    "file": "",
    "drive": "",
    "year": 2016}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "朱盈樺"
pp["name"]["eng"] = "Ying-Hua Chu"
pp["year"] = 17
pp["degrees"][0] = {"chi": "國立台灣大學 學士", "eng": "B.S., National Taiwan University (15)"}
pp["degrees"][1] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (17)"}
pp["jobs"][0] = {
    "chi": "永宏電機股份有限公司", 
    "eng": "FATEK Automation Corporation", 
    "web": "http://www.fatek.com/en/"}
pp["thesis"] = {
    "chi": "動態行為之參數辨識與校正", 
    "eng": "Uncertainty Parameter Identification and Calibration in Dynamic Performances", 
    "file": "ChuYingHua.pdf", 
    "drive": "https://drive.google.com/open?id=1N7YUV68kbeGGhi0VAsaLKqAtaIU4VH04"}
pp["papers"][0] = {
    "ref": """Y.-H. Chu and K.-Y. Chan, "Uncertainty Parameter Identification and Calibration in Dynamic Performances", International Workshop on Reliability for Advanced Technology, Taipei, Taiwan, Feb 16, 2017""",
    "file": "",
    "drive": "",
    "type": "ic",
    "year": 2017}
data[i] = pp

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "張顯主"
pp["name"]["eng"] = "Xian-Zhu Chong"
pp["year"] = 17
pp["degrees"][0] = {"chi": "國立台灣大學 學士", "eng": "B.S., National Taiwan University (15)"}
pp["degrees"][1] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (18)"}
pp["jobs"][0] = {
    "chi": "鼎天國際股份有限公司", 
    "eng": "RoyalTek Company Ltd.", 
    "web": "http://www.royaltek.com/"}
pp["thesis"] = {
    "chi": "使用反應曲面以提升電池電量在動態運行下的預測精度", 
    "eng": "Improved State of Charge Estimation of Lithium-Ion Cells via Surrogate Modeling under Dynamic Operating Conditions", 
    "file": "ChongXianZhu.pdf", 
    "drive": "https://drive.google.com/open?id=1Lz1UeP31cz0yOEOruxich7D-I-9dAy43"}
pp["papers"][0] = {
    "ref": """J. Chong and K.-Y. Chan, "Improved State of Charge Estimation of Lithium-ion Battery via Surrogate Modeling Under Dynamic Operating Conditions", International Workshop on Reliability for Advanced Technology, Feb 16, 2017, Taipei, Taiwan""",
    "file": "",
    "drive": "",
    "type": "ic",
    "year": 2017}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "蔡穎寬"
pp["name"]["eng"] = "Ying-Kuan Tsai"
pp["year"] = 18
pp["degrees"][0] = {"chi": "國立臺灣科技大學 學士", "eng": "B.S., National Taiwan University of Science and Technology (16)"}
pp["degrees"][1] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (18)"}
pp["degrees"][2] = {"chi": "美國德州農工大學 博士班學生", "eng": "Ph.D. Student, Texas A&M University (19~)"}
pp["thesis"] = {
    "chi": "垂直多關節機械手臂與並聯式機械手臂之不確定因素評估與工作表現最佳化", 
    "eng": "Uncertainty Estimation and Performance Optimization for Vertical Articulated and Parallel Robot Manipulators", 
    "file": "YingKuanTsai.pdf", 
    "drive": "https://drive.google.com/open?id=1ivC-HnH40XqYlPAtcd4JWi9atGYzP6Dt"}
pp["papers"][0] = {
    "ref": """K.-L. Li, Y.-K. Tsai, and K.-Y. Chan, "Identifying Joint Clearance via Robot Manipulation", Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science 232, no. 15, August, 2018""",
    "file": "2017IdentifyingJointClearanceViaRobotManipulation.pdf",
    "drive": "https://drive.google.com/open?id=1SQ-gNonKEOLpVgICCrkjjzgYB8nFnYLB",
    "type": "j",
    "year": 2018}
pp["papers"][1] = {
    "ref": """Y.-K. Tsai, and K.-Y. Chan, "Uncertainty Estimation and Performance Optimal Design for Vertical Articulated Robot Manipulators", the 21st National Conference on Mechanism and Machine Design, National Taiwan Ocean University, Keelung, Taiwan, Oct. 26-27, 2018""",
    "type": "ic",
    "file": "",
    "drive": "",
    "year": 2018}   
pp["papers"][2] = {
    "ref": """Y.-K. Tsai, and K.-Y. Chan, "Investigation on the Impact of Non-geometric Uncertainty in Dynamic Performance of Serial and Parallel Robot Manipulators", Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science, Vol. 233, issue 10, pp.3487-3511, May 1, 2019""",
    "type": "j",
    "file": "2019InvestigationImpactNongeometric_JMES.pdf",
    "drive": "https://drive.google.com/open?id=1FLwBv3VCACFOUL7GMkD8IpLXbd-7Kc5w",
    "year": 2019}
pp["papers"][3] = {
    "ref": """Y.-K. Tsai, and K.-Y. Chan, "Parameter Identification and Performance Optimization for Vertical Articulated Robot Manipulators under Transmission Uncertainty for Harmonic Drives", submitted to ASME. Journal of Mechanical Design, 2018""",
    "type": "j",
    "file": "",
    "drive": "",
    "year": 2018}   

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "李旻憲"
pp["name"]["eng"] = "Min-Hsien Lee"
pp["year"] = 18
pp["degrees"][0] = {"chi": "國立臺灣大學 學士", "eng": "B.S., National Taiwan University (16)"}
pp["degrees"][1] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (18)"}
pp["jobs"][0] = {
    "chi": "新代科技股份有限公司", 
    "eng": "SYNTEC Technology Co. Ltd.", 
    "web": "https://www.syntecclub.com.tw/"}
pp["thesis"] = {
    "chi": "以多重性能偏移特性辨識與校準複雜系統參數之方法", 
    "eng": "Identification and Calibration of Complex Model Parameters via Multiple Performance Deviations", 
    "file": "LeeMinHsien .pdf", 
    "drive": "https://drive.google.com/open?id=1UI-EiW85FZzHUKyxDl5BUn0tBrxSpYrJ"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "林峻廷"
pp["name"]["eng"] = "Chun-Ting Lin"
pp["year"] = 18
pp["degrees"][0] = {"chi": "國立臺灣大學 學士", "eng": "B.S., National Taiwan University (16)"}
pp["degrees"][1] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (18)"}
pp["thesis"] = {
    "chi": "自主駕駛車輛的佔有比對都會混流交通的影響", 
    "eng": "A Study on the Effect of Autonomous Vehicle Penetration Rate in Urban Mix-fleet Traffic", 
    "file": "LinChunTing.pdf", 
    "drive": "https://drive.google.com/open?id=1h1cEqxy63Il_p97xt-4aDefSKTsrS4sD"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "徐世哲"
pp["name"]["eng"] = "Shin-Che Hsu"
pp["year"] = 18
pp["alumni"] = False
pp["lab_id"] = "碩士班學生 M.S. Student"
pp["degrees"][0] = {"chi": "國立臺灣科技大學 學士", "eng": "B.S., National Taiwan University of Science and Technology (16)"}
pp["research"] = {
    "chi": "以振動分析模擬技術提升電動車輛控制器之可靠度", 
    "eng": "Simulation-Based Vibration Analysis for Reliability Improvement of Motor Drive Controllers"}
pp["papers"][0] = {
    "ref": """S.-C. Hsu and K.-Y. Chan, "Simulation-based Vibration Analysis for Reliability Improvement of Motor Drive Controllers", International Workshop on Reliability for Advanced Technology, Taipei, Taiwan, Feb 16, 2017""",
    "file": "",
    "drive": "",
    "type": "ic",
    "year": 2017}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "黃彥智"
pp["name"]["eng"] = "Yeh-Chih Huang"
pp["year"] = 9
pp["alumni"] = False
pp["lab_id"] = "博士候選人 Ph.D. Candidate"
pp["degrees"][0] = {"chi": "國立交通大學 學士", "eng": "B.S., National Chiao Tung University (07)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (09)"}
pp["thesis"] = {
    "chi": "針對機率拘束空間內最大可靠度問題之 EGO 演算法修正", 
    "eng": "A Modified Efficient Global Optimization Algorithm for Maximal Reliability in a Probabilistic Constrained Space", 
    "file": "HuangYenChih.pdf", 
    "drive": "https://drive.google.com/open?id=1L1nhqYLK1nobKftAjdLjzQnIsHtoA1F_"}
pp["papers"][0] = {
    "ref": """K.-Y. Chan and Y.-C. Huang, "An Active Set Sequential Quadratic Programming with Variable Probabilistic Constraint Evaluations for Optimization Problems under Non-Gaussian Uncertainties", Journal of Mechanical Engineering Science 226(6), pp.1273-1285, 2010""",
    "file": "2010JMES_NonGaussian.pdf",
    "drive": "https://drive.google.com/open?id=1SArUSYEkxk4v8f9bBzQgUK_xOmdsk6CE",
    "type": "j",
    "year": 2010}
pp["papers"][1] = {
    "ref": """Y.-C. Huang and K.-Y. Chan, "A Modified Efficient Global Optimization Algorithm for Maximal Reliability in a Probabilistic Constrained Space", Journal of Mechanical Design, 132(6), 061002, 2010""",
    "file": "2010EGO_MaxRel_JMD.pdf",
    "drive": "https://drive.google.com/open?id=1SgC0DMPrXZJm9EM1NC5fG5K_KNLSgf1W",
    "type": "j",
    "year": 2010}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "劉員成"
pp["name"]["eng"] = "Yuan-Cheng Liu"
pp["year"] = 19
pp["alumni"] = True
pp["degrees"][0] = {"chi": "國立臺灣大學 學士", "eng": "B.S., National Taiwan University (17)"}
pp["degrees"][1] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (19)"}
pp["research"] = {
    "chi": "以機率模型預測在都市十字路口的駕駛行為", 
    "eng": "Probabilistic Modeling and Prediction of Driver Behaviors at Urban Crossroads"}
pp["papers"][0] = {
    "ref": """Y.-C. Liu and K.-Y. Chan, "Probabilistic Modeling of Driver Behaviors at Urban Crossroads", Proceedings of the ASME 2019 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference, Anaheim, California, USA, Aug. 18-21, 2019""",
    "file": "2019_ASME_IDETC_LiuYC.pdf",
    "drive": "https://drive.google.com/open?id=12dFu2aELoGUm9u3HXbIBcGlOZRKCfMb6",
    "type": "ic",
    "year": 2019}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "陳柏宇"
pp["name"]["eng"] = "Po-Yu Chen"
pp["year"] = 19
pp["alumni"] = True
pp["degrees"][0] = {"chi": "國立臺灣科技大學 學士", "eng": "B.S., National Taiwan University of Science and Technology (17)"}
pp["degrees"][1] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (19)"}
pp["research"] = {
    "chi": "", 
    "eng": "Pose Calibration with Machine Vision for Uncertainty Modeling of Cyber-Physical Robot Systems"}
pp["papers"][0] = {
    "ref": """P.-Y. Chen and K.-Y. Chan, "Improving Hole-Searching Accuracy for Peg-in-Hole Assemble with Manipulator Harmonic Drive Uncertainty", Proceedings of the ASME 2019 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference, Anaheim, California, USA, Aug. 18-21, 2019""",
    "file": "2019_ASME_IDETC_chenpy.pdf",
    "drive": "https://drive.google.com/open?id=1TMQWxSShVW-OpSnSfoerCChZnAYEeVhn",
    "type": "ic",
    "year": 2019}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "蔡心婷"
pp["name"]["eng"] = "Hsin-Ting Tsai"
pp["year"] = 19
pp["alumni"] = True
pp["degrees"][0] = {"chi": "國立中央大學 學士", "eng": "B.S., National Central University (17)"}
pp["degrees"][1] = {"chi": "國立臺灣大學 碩士", "eng": "M.S., National Taiwan University (19)"}
pp["research"] = {
    "chi": "感測器誤差對自駕車變換車道策略的敏感性評估", 
    "eng": "Assessing the sensitivity of sensor uncertainty to autonomous vehicle driving strategies during lane change maneuver"}
pp["papers"][0] = {
    "ref": """H.-T. Tsai and K.-Y. Chan, "Investigating the Impact of Component Uncertainty on Autonomous Vehicles Overtaking Maneuvers", Proceedings of the ASME 2019 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference, Anaheim, California, USA, Aug. 18-21, 2019""",
    "file": "2019_ASME_IDETC_tsaiht.pdf",
    "drive": "https://drive.google.com/open?id=1G2ze7S7TR6L-j0hAJ_5JnJFXJ2XyJyku",
    "type": "ic",
    "year": 2019}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "陳怡平"
pp["name"]["eng"] = "Yi-Ping Chen"
pp["year"] = 20
pp["alumni"] = False
pp["lab_id"] = "碩士班學生 M.S. Student"
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (18)"}
pp["research"] = {
    "chi": "用於車輛設計中的不確定因素及失效檢測方法", 
    "eng": "Uncertainty Modeling and Failure Identification in Vehicle Design"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "吳中信"
pp["name"]["eng"] = "Chung-Hsin Wu"
pp["year"] = 20
pp["alumni"] = False
pp["lab_id"] = "碩士班學生 M.S. Student"
pp["degrees"][0] = {"chi": "國立清華大學 學士", "eng": "B.S., National Tsing Hua University (18)"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "陳奕憲"
pp["name"]["eng"] = "Yi-Sian Chen"
pp["year"] = 20
pp["alumni"] = False
pp["lab_id"] = "碩士班學生 M.S. Student"
pp["degrees"][0] = {"chi": "國立中山大學 學士", "eng": "B.S., National Sun Yat-sen University (18)"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "陳宥廷"
pp["name"]["eng"] = "Yu-Ting Chen"
pp["year"] = 20
pp["alumni"] = False
pp["lab_id"] = "碩士班學生 M.S. Student"
pp["degrees"][0] = {"chi": "國立臺灣大學 學士", "eng": "B.S., National Taiwan University (18)"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "肖路寧"
pp["name"]["eng"] = "Lu-Ning Xiao"
pp["year"] = 20
pp["alumni"] = False
pp["lab_id"] = "碩士班學生 M.S. Student"
pp["degrees"][0] = {"chi": "中原大學 學士", "eng": "B.S., Chung Yuan Christian University (18)"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "吳驊祐"
pp["name"]["eng"] = "Hua-Yu Wu"
pp["year"] = 20
pp["alumni"] = False
pp["lab_id"] = "博士班學生 Ph.D. Student"
pp["degrees"][0] = {"chi": "國立成功大學 學士", "eng": "B.S., National Cheng Kung University (11)"}
pp["degrees"][1] = {"chi": "國立成功大學 碩士", "eng": "M.S., National Cheng Kung University (15)"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "呂冠頡"
pp["name"]["eng"] = "Kuan-Chieh Lu"
pp["year"] = 20
pp["alumni"] = True
pp["lab_id"] = "研究助理 Research Assistant"
pp["degrees"][0] = {"chi": "國立臺灣大學 學士", "eng": "B.S., National Taiwan University (18)"}
pp["degrees"][1] = {"chi": "美國伊利諾大學 碩士班學生", "eng": "M.S. Student, University of Illinois, Urbana-Champaign (19~)"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "鍾慕提"
pp["name"]["eng"] = "Mu-Ti Chung"
pp["year"] = 20
pp["alumni"] = True
pp["lab_id"] = "研究助理 Research Assistant"
pp["degrees"][0] = {"chi": "國立臺灣大學 學士", "eng": "B.S., National Taiwan University (18)"}
pp["degrees"][1] = {"chi": "美國密西根大學 碩士班學生", "eng": "M.S. Student, The University of Michigan (19~)"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "林駿汗"
pp["name"]["eng"] = "Chun-Han Lin"
pp["year"] = 21
pp["alumni"] = True
pp["lab_id"] = "專題生 Graduate Student"
pp["degrees"][0] = {"chi": "國立臺灣大學 學士", "eng": "B.S., National Taiwan University (21)"}
pp["research"] = {
    "chi": "四連桿公差制定與動態模擬", 
    "eng": "Four Bar Linkage Mechanism Tolerance Allocation and Dynamic Simulation"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "楊雅媛"
pp["name"]["eng"] = "Ya-Yuan Yang"
pp["year"] = 21
pp["alumni"] = False
pp["lab_id"] = "碩士班學生 M.S. Student"
pp["degrees"][0] = {"chi": "國立中央大學 學士", "eng": "B.S., National Central University (19)"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "李晉毅"
pp["name"]["eng"] = "Jin-Yi Li"
pp["year"] = 21
pp["alumni"] = False
pp["lab_id"] = "碩士班學生 M.S. Student"
pp["degrees"][0] = {"chi": "國立台北科技大學 學士", "eng": "B.S., National Taipei University of Technology (19)"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "李俊杰"
pp["name"]["eng"] = "Jyun-Jie Li"
pp["year"] = 21
pp["alumni"] = False
pp["lab_id"] = "碩士班學生 M.S. Student"
pp["degrees"][0] = {"chi": "國立臺灣大學 學士", "eng": "B.S., National Taiwan University (19)"}

pp.set_first_second()
data[i] = pp

# --

i += 1
pp = tool.People()
pp["name"]["chi"] = "陳昱霖"
pp["name"]["eng"] = "Yu-Lin Chen"
pp["year"] = 21
pp["alumni"] = False
pp["lab_id"] = "碩士班學生 M.S. Student"
pp["degrees"][0] = {"chi": "國立臺灣大學 學士", "eng": "B.S., National Taiwan University (19)"}

pp.set_first_second()
data[i] = pp

# -- 

# i += 1
# pp = tool.People()
# pp["name"]["chi"] = ""
# pp["name"]["eng"] = ""
# pp["year"] = 
# pp["alumni"] = False
# pp["lab_id"] = "碩士班學生 M.S. Student"
# pp["degrees"][0] = {"chi": "", "eng": ""}
# pp["degrees"][1] = {"chi": "", "eng": ""}
# pp["jobs"][0] = {
#     "chi": "", 
#     "eng": "", 
#     "web": ""}
# pp["thesis"] = {
#     "chi": "", 
#     "eng": "", 
#     "file": "", 
#     "drive": ""}
# pp["research"] = {
#     "chi": "", 
#     "eng": ""}
# pp["papers"][0] = {
#     "ref": """""",
#     "file": "",
#     "drive": "",
#     "type": "",
#     "year": }
# pp.set_first_second()
# data[i] = pp

with open('people.json', 'w', encoding='utf-8') as fp:
    json.dump(data, fp, ensure_ascii=False)
    