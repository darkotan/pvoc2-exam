# PVOC 二级游乐船考试刷题网站 — 完整需求文档

## 项目概述
为香港二级游乐船操作人证明书(PVOC Level 2)考试建立一个手机友好的刷题工具。

## 关键资源（已存在）
- 项目目录: `~/pvoc-exam-prep/`
- 官方考试手册PDF: `guide.pdf` (314页, 27MB)
- 官方甲部样卷: `exam_A.pdf` (40题)
- 官方乙部样卷: `exam_B.pdf` (40题)
- 已提取图片: `images/` 目录 (378张官方PDF图片)
- GitHub repo: `darkotan/pvoc2-exam` (gh-pages分支)
- 已部署URL: https://darkotan.github.io/pvoc2-exam/

## 考试规则
- 甲部(航驶/船艺/安全): 40道选择题, 45分钟, 60%合格
- 乙部(轮机知识): 40道选择题, 45分钟, 60%合格
- 两部分独立评分，单科合格成绩保留两年
- 电脑化考试(互动电脑系统)
- 报名: PEAK高峰进修学院 (peak.edu.hk)

## 题目来源（只用真题，不要瞎编）
1. **海事处官方样卷** (最重要):
   - `exam_A.pdf` 甲部40题 (答案: 1D 2D 3B 4B 5C 6C 7A 8B 9A 10C 11D 12B 13A 14A 15D 16B 17C 18B 19C 20C 21C 22C 23B 24D 25B 26A 27B 28B 29B 30B 31D 32D 33D 34A 35B 36B 37A 38A 39D 40A)
   - `exam_B.pdf` 乙部40题 (答案: 1D 2D 3D 4B 5D 6D 7D 8A 9A 10D 11D 12B 13C 14A 15B 16A 17C 18B 19A 20D 21D 22B 23D 24C 25A 26A 27A 28B 29B 30D 31C 32C 33C 34A 35A 36D 37B 38B 39B 40A)
2. **ProProfs DBYC真题库**: 119道英文PVOL题目 (JSON在 `/tmp/pvoc_real_questions.json`)
3. **官方考试手册内容**: 从`guide.pdf`提取的章节内容可用于生成额外题目

## 核心功能需求

### 1. 语言支持
- 简体中文(zh-CN) — 默认
- 繁體中文(zh-TW)
- English(en)
- **关键**: 语言切换必须真正生效，所有题目文本、UI标签、解析都要随语言切换
- 官方题目是繁体中文，需要提供简体翻译
- ProProfs题目是英文，需要提供中英对照

### 2. 学习模式
- **章节练习**: 按章节筛选题目，可选择单章或全部
- **甲部模拟考**: 只出甲部题目(ch1-ch13), 40题/45分钟/60%合格
- **乙部模拟考**: 只出乙部题目(ch14-ch22), 40题/45分钟/60%合格
- **错题回顾**: 考试/练习后可回顾错题

### 3. 题目显示
- 选择题4个选项，选了就不能改(三重保护: guard+无onclick+pointer-events:none)
- 选对显示绿色，选错显示红色，正确答案始终显示绿色
- 答题后显示解析
- 图片题正确显示官方PDF图片(images/目录)

### 4. 章节划分
甲部:
- ch1: 船舶特性 (操纵、冲程、横推力)
- ch2: 锚泊
- ch3: 安全检查 (启航/止航)
- ch4: 海图作业 (定位、罗经差、CADET)
- ch5: 潮汐
- ch6: 有限能见度 (雾号、安全航速)
- ch7: 本地知识 (维港、航道、限速、浮标IALA-A)
- ch8: 避碰规则 (COLREGS: 号灯、号型、声号、避碰行动)
- ch9: 安全设备 (救生衣、灭火器)
- ch10: VHF通讯 (频道、MAYDAY)
- ch11: 海事处服务
- ch12: 暴风信号和气象 (风球、蒲福风级)
- ch13: 紧急应变 (堕海、搁浅、碰撞、火灾)

乙部:
- ch14: 基本原理 (内燃机、四冲程、闪火点)
- ch15: 主机汽油机 (点火、化油器)
- ch16: 主机柴油机 (喷油、压缩点火)
- ch17: 舷外汽油机
- ch18: 辅机 (舵机、泵、电池、发电机)
- ch19: 操作维修 (日常保养、故障排除)
- ch20: 防火安全 (火灾类型、灭火器选择)
- ch21: 石油气安全
- ch22: 环境保护

### 5. 图片题
- 引用images/目录下的官方PDF图片
- 图片必须与题目内容匹配(不要乱引用)
- 已知正确的图片-题目映射:
  - exam_A_p1_img1.png → W/R/G灯光颜色编码
  - exam_A_p1_img2.png → Q1号灯配置(左舷30度)
  - exam_A_p2_img1.png → Q3号灯(右舷两位)
  - exam_A_p3_img1.png → Q5号灯(右舷五位)
  - exam_A_p3_img2.png → Q6对遇号灯
  - exam_A_p3_img3.png → Q7左舷三位号灯
  - exam_A_p4_img1.png → Q8左舷一位号灯
  - exam_A_p6_img1.png → Q19航海标志(潜水员旗)
  - exam_A_p7_img1.png → Q20香港海图(VTC区域)
  - exam_A_p7_img2.png → Q20海图细节
  - exam_A_p9_img1.png → Q26绿色锥形浮标
  - exam_B_p2_img1.jpeg → Q1内燃机行程图
  - exam_B_p7_img1.png → Q22活塞泵阀门图

### 6. 考试规则/信息页
- 显示考试规则、报名方式、合格标准
- PEAK报名链接

### 7. UI设计
- 移动端友好(手机5G直接访问)
- 暗色/亮色主题(跟随系统)
- 进度条显示答题进度
- 计时器(考试模式)
- 简洁清爽的设计

## 技术要求
- 纯HTML单文件(index.html), localStorage保存进度
- 部署在GitHub Pages(gh-pages分支)
- 图片在images/目录，相对路径引用
- 推送命令: `git push origin gh-pages`

## 题目JSON格式
```json
{
  "ch": "ch8",
  "q": {"zh-CN": "简体题目", "zh-TW": "繁體題目", "en": "English question"},
  "o": [
    {"zh-CN": "选项A", "zh-TW": "選項A", "en": "Option A"},
    {"zh-CN": "选项B", "zh-TW": "選項B", "en": "Option B"},
    {"zh-CN": "选项C", "zh-TW": "選項C", "en": "Option C"},
    {"zh-CN": "选项D", "zh-TW": "選項D", "en": "Option D"}
  ],
  "a": 0,
  "exp": {"zh-CN": "解析", "zh-TW": "解析", "en": "Explanation"},
  "img": "exam_A_p1_img1.png"
}
```
- `a`: 正确答案索引(0=A, 1=B, 2=C, 3=D)
- `img`: 可选，图片文件名(在images/目录下)

## 禁止事项
- 不要瞎编题目，只用真实考试来源
- 不要中英文混在一起(语言切换时全部统一)
- 不要把甲部乙部题目混在模拟考里
- 不要引用不存在的图片
