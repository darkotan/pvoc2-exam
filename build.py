#!/usr/bin/env python3
"""Build script for PVOC exam prep. Generates a single index.html with all data embedded."""

import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))

def load_json(path):
    with open(os.path.join(BASE, path), 'r', encoding='utf-8') as f:
        return json.load(f)

def safe_load(path):
    try:
        return load_json(path)
    except:
        return []

# Traditional → Simplified character map (comprehensive)
T2S = {
    '機':'机','關':'关','號':'号','燈':'灯','運':'运','轉':'转','聲':'声','圖':'图',
    '選':'选','項':'项','點':'点','線':'线','記':'记','設':'设','變':'变','資':'资',
    '輪':'轮','載':'载','輕':'轻','過':'过','達':'达','遠':'远','適':'适','邊':'边',
    '鐘':'钟','門':'门','開':'开','間':'间','陣':'阵','隨':'随','險':'险','雖':'虽',
    '雙':'双','雜':'杂','離':'离','難':'难','雲':'云','電':'电','靈':'灵','靜':'静',
    '響':'响','順':'顺','預':'预','頭':'头','題':'题','額':'额','風':'风','飛':'飞',
    '養':'养','餘':'余','駕':'驾','驗':'验','體':'体','魚':'鱼','黃':'黄','齊':'齐',
    '龍':'龙','與':'与','業':'业','東':'东','練':'练','結':'结','絕':'绝','總':'总',
    '續':'续','網':'网','義':'义','習':'习','聯':'联','聖':'圣','聞':'闻','職':'职',
    '華':'华','萬':'万','節':'节','書':'书','廠':'厂','廣':'广','慶':'庆','應':'应',
    '戰':'战','戲':'戏','據':'据','擔':'担','濟':'济','濤':'涛','燈':'灯','營':'营',
    '環':'环','當':'当','盡':'尽','劃':'划','劇':'剧','團':'团','執':'执','報':'报',
    '場':'场','塊':'块','堅':'坚','備':'备','夢':'梦','夠':'够','奪':'夺','婦':'妇',
    '審':'审','寫':'写','寬':'宽','層':'层','歲':'岁','島':'岛','嶺':'岭','幣':'币',
    '師':'师','帳':'帐','帶':'带','幫':'帮','幹':'干','幾':'几','庫':'库','廠':'厂',
    '彈':'弹','彎':'弯','態':'态','憐':'怜','戰':'战','擁':'拥','擋':'挡','擠':'挤',
    '擬':'拟','敵':'敌','數':'数','斷':'断','昇':'升','書':'书','會':'会','桿':'杆',
    '條':'条','楊':'杨','業':'业','極':'极','構':'构','歸':'归','歲':'岁','歷':'历',
    '殺':'杀','殼':'壳','氣':'气','決':'决','沖':'冲','況':'况','淨':'净','淵':'渊',
    '測':'测','準':'准','溝':'沟','溫':'温','滅':'灭','漁':'渔','漲':'涨','潔':'洁',
    '燈':'灯','營':'营','爺':'爷','爾':'尔','牆':'墙','獎':'奖','獨':'独','獲':'获',
    '環':'环','異':'异','療':'疗','盜':'盗','盡':'尽','監':'监','碼':'码','確':'确',
    '礎':'础','禍':'祸','積':'积','穩':'稳','競':'竞','筆':'笔','範':'范','築':'筑',
    '簡':'简','籃':'篮','糧':'粮','約':'约','級':'级','紋':'纹','純':'纯','細':'细',
    '組':'组','結':'结','給':'给','絕':'绝','統':'统','維':'维','網':'网','編':'编',
    '緣':'缘','練':'练','縣':'县','縱':'纵','總':'总','繩':'绳','繪':'绘','繫':'系',
    '續':'续','纜':'缆','罈':'坛','罰':'罚','習':'习','聖':'圣','聯':'联','聲':'声',
    '職':'职','聽':'听','肅':'肃','脅':'胁','脫':'脱','膠':'胶','臨':'临','臺':'台',
    '興':'兴','舊':'旧','號':'号','蟲':'虫','補':'补','製':'制','複':'复','規':'规',
    '視':'视','親':'亲','觀':'观','計':'计','訊':'讯','託':'托','記':'记','設':'设',
    '許':'许','訴':'诉','診':'诊','詞':'词','試':'试','詩':'诗','話':'话','該':'该',
    '詳':'详','語':'语','誤':'误','說':'说','請':'请','課':'课','調':'调','談':'谈',
    '論':'论','請':'请','諸':'诸','讀':'读','護':'护','變':'变','豐':'丰','負':'负',
    '財':'财','貢':'贡','貨':'货','販':'贩','貪':'贪','貫':'贯','責':'责','貴':'贵',
    '買':'买','費':'费','貼':'贴','資':'资','質':'质','購':'购','賽':'赛','贊':'赞',
    '趕':'赶','趙':'赵','跡':'迹','車':'车','軍':'军','軟':'软','較':'较','載':'载',
    '輕':'轻','輛':'辆','輩':'辈','輪':'轮','輯':'辑','輸':'输','辦':'办','邊':'边',
    '達':'达','違':'违','遠':'远','適':'适','選':'选','遼':'辽','還':'还','邁':'迈',
    '運':'运','過':'过','遞':'递','遲':'迟','邊':'边','鄭':'郑','鄰':'邻','醫':'医',
    '釋':'释','量':'量','鑒':'鉴','銀':'银','銅':'铜','銘':'铭','銷':'销','鋁':'铝',
    '錄':'录','錯':'错','鍋':'锅','鍛':'锻','鍵':'键','鎖':'锁','鏡':'镜','鐘':'钟',
    '鑰':'钥','鑲':'镶','門':'门','閃':'闪','閉':'闭','問':'问','開':'开','閑':'闲',
    '間':'间','閣':'阁','閱':'阅','閻':'阎','闆':'板','闊':'阔','關':'关','闡':'阐',
    '隊':'队','陣':'阵','陰':'阴','陳':'陈','陽':'阳','隨':'随','險':'险','隱':'隐',
    '難':'难','雄':'雄','雜':'杂','雞':'鸡','離':'离','難':'难','雲':'云','電':'电',
    '霧':'雾','靈':'灵','靜':'静','韋':'韦','響':'响','頁':'页','頂':'顶','項':'项',
    '順':'顺','須':'须','預':'预','頑':'顽','頓':'顿','頗':'颇','領':'领','頭':'头',
    '頻':'频','題':'题','額':'额','顏':'颜','願':'愿','顯':'显','風':'风','飛':'飞',
    '飢':'饥','飯':'饭','飲':'饮','飾':'饰','飽':'饱','餓':'饿','餘':'余','館':'馆',
    '首':'首','香':'香','馬':'马','駁':'驳','駐':'驻','駕':'驾','駛':'驶','駝':'驼',
    '駭':'骇','驗':'验','騎':'骑','騙':'骗','驅':'驱','驕':'骄','魚':'鱼','鮮':'鲜',
    '鳥':'鸟','鳳':'凤','鳴':'鸣','鴨':'鸭','鷹':'鹰','鹽':'盐','麗':'丽','麥':'麦',
    '麼':'么','黃':'黄','點':'点','黨':'党','鼓':'鼓','齊':'齐','齒':'齿','齡':'龄',
    '龍':'龙','龜':'龟','龐':'庞','廳':'厅','輛':'辆','鏈':'链','軟':'软','較':'较',
    '輕':'轻','輛':'辆','輩':'辈','輪':'轮','輯':'辑','輸':'输','辦':'办','邊':'边',
    '噸':'吨','嚮':'向','圍':'围','圖':'图','團':'团','執':'执','報':'报','場':'场',
    '塊':'块','堅':'坚','備':'备','夢':'梦','夠':'够','奪':'夺','婦':'妇','審':'审',
    '寫':'写','寬':'宽','層':'层','歲':'岁','島':'岛','嶺':'岭','幣':'币','師':'师',
    '帳':'帐','帶':'带','幫':'帮','幹':'干','幾':'几','庫':'库','廣':'广','慶':'庆',
    '應':'应','戰':'战','戲':'戏','據':'据','擔':'担','濟':'济','濤':'涛','營':'营',
    '環':'环','當':'当','盡':'尽','劃':'划','劇':'剧','穩':'稳','競':'竞','筆':'笔',
    '範':'范','築':'筑','簡':'简','籃':'篮','糧':'粮','約':'约','級':'级','紋':'纹',
    '純':'纯','細':'细','組':'组','結':'结','給':'给','絕':'绝','統':'统','維':'维',
    '網':'网','編':'编','緣':'缘','練':'练','縣':'县','縱':'纵','總':'总','繩':'绳',
    '繪':'绘','繫':'系','續':'续','纜':'缆','罈':'坛','罰':'罚','習':'习','聖':'圣',
    '聯':'联','聲':'声','職':'职','聽':'听','肅':'肃','脅':'胁','脫':'脱','膠':'胶',
    '臨':'临','臺':'台','興':'兴','舊':'旧','蟲':'虫','補':'补','製':'制','複':'复',
    '規':'规','視':'视','親':'亲','觀':'观','計':'计','訊':'讯','託':'托','記':'记',
    '設':'设','許':'许','訴':'诉','診':'诊','詞':'词','試':'试','詩':'诗','話':'话',
    '該':'该','詳':'详','語':'语','誤':'误','說':'说','請':'请','課':'课','調':'调',
    '談':'谈','論':'论','請':'请','諸':'诸','讀':'读','護':'护','變':'变','豐':'丰',
    '負':'负','財':'财','貢':'贡','貨':'货','販':'贩','貪':'贪','貫':'贯','責':'责',
    '貴':'贵','買':'买','費':'费','貼':'贴','資':'资','質':'质','購':'购','賽':'赛',
    '贊':'赞','趕':'赶','趙':'赵','跡':'迹','車':'车','軍':'军','軟':'软','較':'较',
    '載':'载','輕':'轻','輛':'辆','輩':'辈','輪':'轮','輯':'辑','輸':'输','遲':'迟',
    '還':'还','鉛':'铅','閥':'阀','須':'须','駁':'驳','墮':'堕','擱':'搁','擲':'掷',
    '擬':'拟','擺':'摆','擾':'扰','敵':'敌','數':'数','層':'层','嶼':'屿','廠':'厂',
    '廣':'广','彈':'弹','彎':'弯','態':'态','憐':'怜','擁':'拥','擠':'挤','損':'损',
    '據':'据','撿':'捡','擔':'担','斃':'毙','於':'于','昇':'升','書':'书','會':'会',
    '桿':'杆','條':'条','楊':'杨','業':'业','極':'极','構':'构','歸':'归','歷':'历',
    '殺':'杀','殼':'壳','氣':'气','決':'决','沖':'冲','況':'况','淨':'净','淵':'渊',
    '測':'测','準':'准','溝':'沟','溫':'温','滅':'灭','漁':'渔','漲':'涨','潔':'洁',
    '爺':'爷','爾':'尔','牆':'墙','獎':'奖','獨':'独','獲':'获','異':'异','療':'疗',
    '盜':'盗','盡':'尽','監':'监','碼':'码','確':'确','礎':'础','禍':'祸','積':'积',
    '穩':'稳','競':'竞','筆':'笔','範':'范','築':'筑','簡':'简','籃':'篮','糧':'粮',
    '紗':'纱','純':'纯','細':'细','組':'组','結':'结','給':'给','絕':'绝','統':'统',
    '維':'维','網':'网','編':'编','緣':'缘','練':'练','縣':'县','縱':'纵','總':'总',
    '繩':'绳','繪':'绘','繫':'系','續':'续','纜':'缆','罈':'坛','罰':'罚','習':'习',
    '聖':'圣','聯':'联','聲':'声','職':'职','聽':'听','肅':'肃','脅':'胁','脫':'脱',
    '膠':'胶','臨':'临','臺':'台','興':'兴','舊':'旧','蟲':'虫','補':'补','製':'制',
    '複':'复','規':'规','視':'视','親':'亲','觀':'观','計':'计','訊':'讯','託':'托',
    '記':'记','設':'设','許':'许','訴':'诉','診':'诊','詞':'词','試':'试','詩':'诗',
    '話':'话','該':'该','詳':'详','語':'语','誤':'误','說':'说','請':'请','課':'课',
    '調':'调','談':'谈','論':'论','請':'请','諸':'诸','讀':'读','護':'护','變':'变',
    '豐':'丰','負':'负','財':'财','貢':'贡','貨':'货','販':'贩','貪':'贪','貫':'贯',
    '責':'责','貴':'贵','買':'买','費':'费','貼':'贴','資':'资','質':'质','購':'购',
    '賽':'赛','贊':'赞','趕':'赶','趙':'赵','跡':'迹','車':'车','軍':'军','軟':'软',
    '較':'较','載':'载','輕':'轻','輛':'辆','輩':'辈','輪':'轮','輯':'辑','輸':'输',
}

def t2s(text):
    """Convert Traditional Chinese to Simplified Chinese."""
    return ''.join(T2S.get(c, c) for c in text)

def build_questions():
    """Build unified question array from all sources."""
    exam_a = safe_load('data_exam_a.json')
    exam_b = safe_load('data_exam_b.json')
    proprofs = safe_load('data_proprofs_real.json')

    trans_a = safe_load('trans_exam_a.json')
    trans_b = safe_load('trans_exam_b.json')
    trans_pa = safe_load('trans_proprofs_a.json')
    trans_pb = safe_load('trans_proprofs_b.json')

    # Index translations by qnum/idx
    ta = {t['qnum']: t for t in trans_a} if trans_a else {}
    tb = {t['qnum']: t for t in trans_b} if trans_b else {}
    tp = {}
    for t in trans_pa + trans_pb:
        tp[t['idx']] = t

    questions = []

    # Process Exam A
    for q in exam_a:
        qn = q['qnum']
        t = ta.get(qn, {})
        questions.append({
            'id': f'A{qn}',
            'ch': t.get('ch', 'ch8'),
            'q': {'zh-TW': q['q'], 'zh-CN': t2s(q['q']), 'en': t.get('en', q['q'])},
            'o': [{'zh-TW': q['o'][i], 'zh-CN': t2s(q['o'][i]), 'en': t.get('en_o', q['o'])[i] if t.get('en_o') else q['o'][i]} for i in range(4)],
            'a': q['a'],
            'exp': {'zh-TW': t.get('zhTW_exp', ''), 'zh-CN': t.get('zhCN_exp', ''), 'en': t.get('en_exp', '')},
            'img': t.get('img')
        })

    # Process Exam B
    for q in exam_b:
        qn = q['qnum']
        t = tb.get(qn, {})
        questions.append({
            'id': f'B{qn}',
            'ch': t.get('ch', 'ch14'),
            'q': {'zh-TW': q['q'], 'zh-CN': t2s(q['q']), 'en': t.get('en', q['q'])},
            'o': [{'zh-TW': q['o'][i], 'zh-CN': t2s(q['o'][i]), 'en': t.get('en_o', q['o'])[i] if t.get('en_o') else q['o'][i]} for i in range(4)],
            'a': q['a'],
            'exp': {'zh-TW': t.get('zhTW_exp', ''), 'zh-CN': t.get('zhCN_exp', ''), 'en': t.get('en_exp', '')},
            'img': None
        })

    # Process ProProfs
    for idx, q in enumerate(proprofs):
        t = tp.get(idx, {})
        orig_q = q.get('q', {})
        orig_o = q.get('o', [{}]*4)
        orig_exp = q.get('exp', {})
        questions.append({
            'id': f'P{idx}',
            'ch': q.get('ch', 'ch8'),
            'q': {
                'zh-CN': t.get('zhCN', orig_q.get('zh-CN', orig_q.get('en', ''))),
                'zh-TW': t.get('zhTW', orig_q.get('zh-TW', orig_q.get('en', ''))),
                'en': orig_q.get('en', '')
            },
            'o': [{
                'zh-CN': t.get('zhCN_o', [o.get('zh-CN', o.get('en','')) for o in orig_o])[i] if t.get('zhCN_o') else orig_o[i].get('zh-CN', orig_o[i].get('en','')),
                'zh-TW': t.get('zhTW_o', [o.get('zh-TW', o.get('en','')) for o in orig_o])[i] if t.get('zhTW_o') else orig_o[i].get('zh-TW', orig_o[i].get('en','')),
                'en': orig_o[i].get('en', '')
            } for i in range(4)],
            'a': q.get('a', 0),
            'exp': {
                'zh-CN': t.get('zhCN_exp', orig_exp.get('zh-CN', '')),
                'zh-TW': t.get('zhTW_exp', orig_exp.get('zh-TW', '')),
                'en': orig_exp.get('en', '')
            },
            'img': q.get('img')
        })

    return questions

HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>PVOC二级游乐船考试准备</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#f5f5f0;--card:#fff;--primary:#1a5276;--primary-light:#2980b9;
  --success:#27ae60;--danger:#c0392b;--warn:#f39c12;--text:#2c3e50;
  --text-light:#7f8c8d;--border:#dce1e6;--shadow:0 2px 8px rgba(0,0,0,.08);
  --header-bg:linear-gradient(135deg,var(--primary),var(--primary-light));
}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text);line-height:1.6;min-height:100vh;padding-bottom:env(safe-area-inset-bottom)}
.header{background:var(--header-bg);color:#fff;padding:14px 16px;position:sticky;top:0;z-index:100;box-shadow:var(--shadow)}
.header-top{display:flex;justify-content:space-between;align-items:center}
.header h1{font-size:17px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-right:8px}
.controls{display:flex;gap:6px;align-items:center;flex-shrink:0}
.lang-btn{background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3);color:#fff;padding:3px 10px;border-radius:4px;font-size:12px;cursor:pointer;transition:all .15s}
.lang-btn.active{background:#fff;color:var(--primary);font-weight:600}
.theme-btn{background:none;border:none;color:#fff;font-size:18px;cursor:pointer;padding:4px}
.progress-bar{height:3px;background:rgba(255,255,255,.25);border-radius:2px;overflow:hidden;margin-top:8px}
.progress-fill{height:100%;background:var(--success);transition:width .3s;width:0}
.stats-bar{display:flex;gap:10px;margin-top:6px;font-size:11px;opacity:.85;flex-wrap:wrap}

/* Pages */
.page{display:none;padding:16px;max-width:640px;margin:0 auto;animation:fadeIn .2s}
.page.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}

/* Menu */
.mode-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0}
.mode-btn{background:var(--card);border:2px solid var(--border);border-radius:12px;padding:18px 12px;text-align:center;cursor:pointer;transition:all .15s}
.mode-btn:active{transform:scale(.97)}
.mode-btn h3{font-size:15px;margin-bottom:3px}
.mode-btn p{font-size:12px;color:var(--text-light)}
.section-title{font-size:15px;font-weight:700;margin:16px 0 8px;color:var(--text)}

/* Chapter cards */
.ch-card{background:var(--card);border-radius:10px;padding:14px 16px;margin-bottom:8px;box-shadow:var(--shadow);cursor:pointer;display:flex;justify-content:space-between;align-items:center;border-left:4px solid var(--primary);transition:all .15s}
.ch-card:active{transform:scale(.98)}
.ch-card .ch-name{font-size:14px;font-weight:600}
.ch-card .ch-desc{font-size:12px;color:var(--text-light);margin-top:2px}
.ch-card .ch-count{font-size:13px;color:var(--primary);font-weight:600;flex-shrink:0;margin-left:8px}
.ch-card .ch-progress{font-size:11px;color:var(--text-light)}

/* Question */
.q-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;font-size:13px;color:var(--text-light)}
.q-chapter{background:var(--primary);color:#fff;padding:2px 8px;border-radius:4px;font-size:11px}
.q-body{background:var(--card);border-radius:12px;padding:18px;box-shadow:var(--shadow);margin-bottom:12px}
.q-text{font-size:15px;font-weight:500;line-height:1.75}
.q-img-wrap{text-align:center;margin:12px 0}
.q-img{max-width:100%;max-height:300px;border-radius:8px;border:1px solid var(--border)}
.options{display:flex;flex-direction:column;gap:8px;margin-bottom:14px}
.option{background:var(--card);border:2px solid var(--border);border-radius:10px;padding:12px 14px;cursor:pointer;display:flex;align-items:flex-start;gap:10px;font-size:14px;user-select:none;-webkit-tap-highlight-color:transparent;transition:all .12s;line-height:1.55}
.option:active:not(.locked){transform:scale(.98)}
.option .letter{width:26px;height:26px;border-radius:50%;border:2px solid var(--border);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;flex-shrink:0;margin-top:1px}
.option.selected{border-color:var(--primary);background:rgba(26,82,118,.08)}.option.selected .letter{background:var(--primary);color:#fff;border-color:var(--primary)}
.option.correct{border-color:var(--success);background:rgba(39,174,96,.08)}.option.correct .letter{background:var(--success);color:#fff;border-color:var(--success)}
.option.wrong{border-color:var(--danger);background:rgba(192,57,43,.08)}.option.wrong .letter{background:var(--danger);color:#fff;border-color:var(--danger)}
.option.locked{cursor:default;pointer-events:none;opacity:.85}
.explanation{background:rgba(243,156,18,.08);border:1px solid rgba(243,156,18,.3);border-radius:10px;padding:14px;margin-bottom:14px;font-size:13.5px;line-height:1.7;display:none}
.explanation.show{display:block;animation:fadeIn .2s}
.explanation .exp-label{font-weight:700;color:var(--warn);margin-bottom:4px;font-size:13px}

/* Navigation */
.nav-bar{display:flex;gap:8px;margin-bottom:16px}
.nav-btn{flex:1;padding:13px;border:none;border-radius:10px;font-size:14px;font-weight:600;cursor:pointer;transition:all .15s}
.nav-btn:active{transform:scale(.97)}
.nav-btn.prev{background:var(--card);border:2px solid var(--border);color:var(--text)}
.nav-btn.next{background:var(--primary);color:#fff}
.nav-btn:disabled{opacity:.35;cursor:default;transform:none}

/* Timer */
.timer-bar{display:none;position:fixed;bottom:0;left:0;right:0;background:var(--card);border-top:2px solid var(--border);padding:10px 16px;text-align:center;font-size:14px;font-weight:600;z-index:100;box-shadow:0 -2px 8px rgba(0,0,0,.1)}
.timer-bar.show{display:block}
.timer-warn{color:var(--danger)}

/* Results */
.result-card{background:var(--card);border-radius:16px;padding:24px;text-align:center;box-shadow:var(--shadow);margin-bottom:14px}
.result-score{font-size:48px;font-weight:800;margin:10px 0}
.result-score.pass{color:var(--success)}.result-score.fail{color:var(--danger)}
.result-bar{height:10px;background:#eee;border-radius:5px;overflow:hidden;margin:10px 0}.result-bar-fill{height:100%;border-radius:5px;transition:width .6s}
.result-msg{font-size:13px;color:var(--text-light);margin:8px 0}
.result-detail{display:flex;justify-content:center;gap:20px;margin-top:12px;font-size:14px}
.result-detail .correct{color:var(--success);font-weight:700}.result-detail .wrong-c{color:var(--danger);font-weight:700}

/* Review list */
.review-item{background:var(--card);border-radius:10px;padding:12px 14px;margin-bottom:8px;box-shadow:var(--shadow);cursor:pointer;border-left:4px solid var(--danger);transition:all .15s}
.review-item:active{transform:scale(.98)}
.review-item .ri-num{font-weight:700;font-size:12px;color:var(--text-light)}
.review-item .ri-text{font-size:13px;margin-top:3px;line-height:1.5}
.review-item .ri-ans{font-size:12px;margin-top:4px}

/* Info page */
.info-block{background:var(--card);border-radius:12px;padding:18px;margin-bottom:12px;box-shadow:var(--shadow)}
.info-block h3{color:var(--primary);margin-bottom:10px;font-size:15px}
.info-block ul{padding-left:18px}.info-block li{margin-bottom:6px;font-size:13.5px;line-height:1.6}
.info-block a{color:var(--primary-light)}

/* Wrong answers page */
.wrong-count{font-size:13px;color:var(--text-light);margin-bottom:12px}
.empty-msg{text-align:center;padding:40px 20px;color:var(--text-light);font-size:14px}

/* Back button */
.back-btn{background:none;border:none;color:var(--primary);font-size:14px;cursor:pointer;padding:8px 0;margin-bottom:8px;font-weight:600}

/* Dark theme */
[data-theme="dark"]{
  --bg:#0f0f1a;--card:#1a1a2e;--text:#e0e0e0;--text-light:#8888a0;
  --border:#2a2a4a;--shadow:0 2px 8px rgba(0,0,0,.3);
  --header-bg:linear-gradient(135deg,#1a3a5c,#2a5a8c);
}
[data-theme="dark"] .option.selected{background:rgba(41,128,185,.15)}
[data-theme="dark"] .option.correct{background:rgba(39,174,96,.15)}
[data-theme="dark"] .option.wrong{background:rgba(192,57,43,.15)}
[data-theme="dark"] .explanation{background:rgba(243,156,18,.1);border-color:rgba(243,156,18,.25)}

@media(max-width:360px){
  .header h1{font-size:15px}.mode-btn{padding:14px 8px}.mode-btn h3{font-size:13px}
}
.bottom-spacer{height:60px}
</style>
</head>
<body>
<div class="header">
  <div class="header-top">
    <h1 id="pageTitle">🚢 二级游乐船考试</h1>
    <div class="controls">
      <button class="lang-btn active" data-lang="zh-CN" onclick="setLang('zh-CN')">简体</button>
      <button class="lang-btn" data-lang="zh-TW" onclick="setLang('zh-TW')">繁體</button>
      <button class="lang-btn" data-lang="en" onclick="setLang('en')">EN</button>
      <button class="theme-btn" onclick="toggleTheme()" id="themeBtn">🌙</button>
    </div>
  </div>
  <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
  <div class="stats-bar" id="statsBar"></div>
</div>

<!-- MENU PAGE -->
<div class="page active" id="menuPage">
  <div class="mode-grid">
    <div class="mode-btn" onclick="startPractice()" style="border-color:var(--primary)">
      <h3 id="tPractice">📝 章节练习</h3><p id="tPracticeD">按章节学习</p>
    </div>
    <div class="mode-btn" onclick="showInfo()" style="border-color:var(--text-light)">
      <h3 id="tInfo">📋 考试规则</h3><p id="tInfoD">报名与合格标准</p>
    </div>
    <div class="mode-btn" onclick="startExamA()" style="border-color:var(--danger)">
      <h3 id="tExamA">📋 甲部模拟考</h3><p id="tExamAD">航驶/船艺/安全 40题</p>
    </div>
    <div class="mode-btn" onclick="startExamB()" style="border-color:#8e44ad">
      <h3 id="tExamB">🔧 乙部模拟考</h3><p id="tExamBD">轮机知识 40题</p>
    </div>
  </div>
  <div class="mode-btn" onclick="showWrong()" style="border-color:var(--danger);margin-top:4px">
    <h3 id="tWrong">❌ 错题回顾</h3><p id="tWrongD">复习做错的题目</p>
  </div>
</div>

<!-- CHAPTER PAGE -->
<div class="page" id="chapterPage">
  <button class="back-btn" onclick="showMenu()" id="tBack1">← 返回</button>
  <h3 class="section-title" id="tChTitle">选择章节</h3>
  <div id="chapterList"></div>
</div>

<!-- QUESTION PAGE -->
<div class="page" id="questionPage">
  <div class="q-header">
    <span><span id="qNum">1</span> / <span id="qTotal">40</span></span>
    <span class="q-chapter" id="qChapter"></span>
  </div>
  <div class="q-body">
    <div class="q-text" id="qText"></div>
    <div class="q-img-wrap" id="qImgWrap" style="display:none"><img class="q-img" id="qImg" src="" alt="" onerror="this.parentElement.style.display='none'"></div>
  </div>
  <div class="options" id="optBox"></div>
  <div class="explanation" id="expBox"><div class="exp-label" id="expLabel">📖 解析</div><div id="expText"></div></div>
  <div class="nav-bar">
    <button class="nav-btn prev" id="btnPrev" onclick="prevQ()">← 上一题</button>
    <button class="nav-btn next" id="btnNext" onclick="nextQ()">下一题 →</button>
  </div>
  <div class="bottom-spacer"></div>
</div>

<!-- TIMER -->
<div class="timer-bar" id="timerBar">⏱️ <span id="timerDisplay">45:00</span></div>

<!-- RESULT PAGE -->
<div class="page" id="resultPage">
  <div class="result-card">
    <div style="font-size:14px;color:var(--text-light)" id="resTitle"></div>
    <div class="result-score" id="resScore">0%</div>
    <div class="result-bar"><div class="result-bar-fill" id="resBarFill"></div></div>
    <div class="result-msg" id="resMsg"></div>
    <div class="result-detail">
      <span>✅ <span class="correct" id="resCorrect">0</span></span>
      <span>❌ <span class="wrong-c" id="resWrong">0</span></span>
    </div>
  </div>
  <h3 class="section-title" id="tReview">错题回顾</h3>
  <div id="reviewList"></div>
  <div class="nav-bar" style="margin-top:14px">
    <button class="nav-btn prev" onclick="showMenu()">🏠 首页</button>
    <button class="nav-btn next" onclick="retryWrong()">🔄 重做错题</button>
  </div>
</div>

<!-- WRONG PAGE -->
<div class="page" id="wrongPage">
  <button class="back-btn" onclick="showMenu()" id="tBack2">← 返回</button>
  <h3 class="section-title" id="tWrongTitle">错题本</h3>
  <div class="wrong-count" id="wrongCount"></div>
  <div id="wrongList"></div>
</div>

<!-- INFO PAGE -->
<div class="page" id="infoPage">
  <button class="back-btn" onclick="showMenu()" id="tBack3">← 返回</button>
  <div class="info-block" id="infoContent"></div>
</div>

<script>
'use strict';

/* ========== DATA ========== */
const ALL_Q = __QUESTIONS_JSON__;

/* ========== TRANSLATIONS ========== */
const T2S_MAP = __T2S_JSON__;

function t2s(text) {
  if (!text) return '';
  let r = '';
  for (let i = 0; i < text.length; i++) {
    r += T2S_MAP[text[i]] || text[i];
  }
  return r;
}

const UI = {
  'zh-CN': {
    title: '🚢 二级游乐船考试', practice: '📝 章节练习', practiceD: '按章节学习',
    examA: '📋 甲部模拟考', examAD: '航驶/船艺/安全 40题',
    examB: '🔧 乙部模拟考', examBD: '轮机知识 40题',
    info: '📋 考试规则', infoD: '报名与合格标准',
    wrong: '❌ 错题回顾', wrongD: '复习做错的题目',
    chTitle: '选择章节', back: '← 返回',
    prev: '← 上一题', next: '下一题 →', submit: '📝 交卷',
    expLabel: '📖 解析', review: '错题回顾', retry: '🔄 重做错题',
    home: '🏠 首页', wrongTitle: '错题本', emptyWrong: '暂无错题，继续加油！',
    passMsg: '🎉 恭喜通过！', failMsg: '💪 继续努力！',
    totalQ: '总题数', doneQ: '已完成', correctQ: '答对', wrongQ: '答错',
    timerWarn: '时间不多了！',
    chNames: {
      ch1:'船舶特性',ch2:'锚泊',ch3:'安全检查',ch4:'海图作业',ch5:'潮汐',
      ch6:'有限能见度',ch7:'本地知识',ch8:'避碰规则',ch9:'安全设备',
      ch10:'VHF通讯',ch11:'海事处服务',ch12:'暴风信号和气象',ch13:'紧急应变',
      ch14:'基本原理',ch15:'主机汽油机',ch16:'主机柴油机',ch17:'舷外汽油机',
      ch18:'辅机',ch19:'操作维修',ch20:'防火安全',ch21:'石油气安全',ch22:'环境保护'
    },
    partA: '甲部 (ch1-ch13)', partB: '乙部 (ch14-ch22)',
    infoHtml: `<h3>📋 考试规则</h3><ul>
      <li><b>甲部(航驶/船艺/安全)</b>：40道选择题，45分钟，60%合格</li>
      <li><b>乙部(轮机知识)</b>：40道选择题，45分钟，60%合格</li>
      <li>两部分独立评分，单科合格成绩保留两年</li>
      <li>电脑化考试(互动电脑系统)</li>
    </ul><h3 style="margin-top:16px">📝 报名方式</h3><ul>
      <li>报名机构：<a href="https://www.peak.edu.hk" target="_blank">PEAK高峰进修学院</a></li>
      <li>查询：2836 0000</li>
    </ul><h3 style="margin-top:16px">📚 考试范围</h3><ul>
      <li><b>甲部</b>：船舶操纵、锚泊、安全检查、海图作业、潮汐、能见度、本地知识、避碰规则、安全设备、VHF通讯、海事处服务、暴风信号、紧急应变</li>
      <li><b>乙部</b>：内燃机原理、汽油机、柴油机、舷外机、辅机、操作维修、防火安全、石油气安全、环境保护</li>
    </ul>`
  },
  'zh-TW': {
    title: '🚢 二級遊樂船考試', practice: '📝 章節練習', practiceD: '按章節學習',
    examA: '📋 甲部模擬考', examAD: '航駛/船藝/安全 40題',
    examB: '🔧 乙部模擬考', examBD: '輪機知識 40題',
    info: '📋 考試規則', infoD: '報名與合格標準',
    wrong: '❌ 錯題回顧', wrongD: '複習做錯的題目',
    chTitle: '選擇章節', back: '← 返回',
    prev: '← 上一題', next: '下一題 →', submit: '📝 交卷',
    expLabel: '📖 解析', review: '錯題回顧', retry: '🔄 重做錯題',
    home: '🏠 首頁', wrongTitle: '錯題本', emptyWrong: '暫無錯題，繼續加油！',
    passMsg: '🎉 恭喜通過！', failMsg: '💪 繼續努力！',
    totalQ: '總題數', doneQ: '已完成', correctQ: '答對', wrongQ: '答錯',
    timerWarn: '時間不多了！',
    chNames: {
      ch1:'船舶特性',ch2:'錨泊',ch3:'安全檢查',ch4:'海圖作業',ch5:'潮汐',
      ch6:'有限能見度',ch7:'本地知識',ch8:'避碰規則',ch9:'安全設備',
      ch10:'VHF通訊',ch11:'海事處服務',ch12:'暴風信號和氣象',ch13:'緊急應變',
      ch14:'基本原理',ch15:'主機汽油機',ch16:'主機柴油機',ch17:'舷外汽油機',
      ch18:'輔機',ch19:'操作維修',ch20:'防火安全',ch21:'石油氣安全',ch22:'環境保護'
    },
    partA: '甲部 (ch1-ch13)', partB: '乙部 (ch14-ch22)',
    infoHtml: `<h3>📋 考試規則</h3><ul>
      <li><b>甲部(航駛/船藝/安全)</b>：40道選擇題，45分鐘，60%合格</li>
      <li><b>乙部(輪機知識)</b>：40道選擇題，45分鐘，60%合格</li>
      <li>兩部分獨立評分，單科合格成績保留兩年</li>
      <li>電腦化考試(互動電腦系統)</li>
    </ul><h3 style="margin-top:16px">📝 報名方式</h3><ul>
      <li>報名機構：<a href="https://www.peak.edu.hk" target="_blank">PEAK高峰進修學院</a></li>
      <li>查詢：2836 0000</li>
    </ul><h3 style="margin-top:16px">📚 考試範圍</h3><ul>
      <li><b>甲部</b>：船舶操縱、錨泊、安全檢查、海圖作業、潮汐、能見度、本地知識、避碰規則、安全設備、VHF通訊、海事處服務、暴風信號、緊急應變</li>
      <li><b>乙部</b>：內燃機原理、汽油機、柴油機、舷外機、輔機、操作維修、防火安全、石油氣安全、環境保護</li>
    </ul>`
  },
  'en': {
    title: '🚢 PVOC Level 2 Exam', practice: '📝 Chapter Study', practiceD: 'Study by chapter',
    examA: '📋 Part A Mock', examAD: 'Navigation/Safety 40Q',
    examB: '📋 Part B Mock', examBD: 'Engineering 40Q',
    info: '📋 Exam Rules', infoD: 'Registration & standards',
    wrong: '❌ Wrong Answers', wrongD: 'Review mistakes',
    chTitle: 'Select Chapter', back: '← Back',
    prev: '← Previous', next: 'Next →', submit: '📝 Submit',
    expLabel: '📖 Explanation', review: 'Wrong Answers Review', retry: '🔄 Retry Wrong',
    home: '🏠 Home', wrongTitle: 'Wrong Answers', emptyWrong: 'No wrong answers yet. Keep it up!',
    passMsg: '🎉 Congratulations!', failMsg: '💪 Keep trying!',
    totalQ: 'Total', doneQ: 'Done', correctQ: 'Correct', wrongQ: 'Wrong',
    timerWarn: 'Time is running out!',
    chNames: {
      ch1:'Vessel Characteristics',ch2:'Anchoring',ch3:'Safety Checks',ch4:'Chart Work',ch5:'Tides',
      ch6:'Restricted Visibility',ch7:'Local Knowledge',ch8:'COLREGS',ch9:'Safety Equipment',
      ch10:'VHF Comms',ch11:'Marine Dept',ch12:'Weather & Signals',ch13:'Emergency',
      ch14:'Basic Principles',ch15:'Petrol Engines',ch16:'Diesel Engines',ch17:'Outboard Engines',
      ch18:'Auxiliary Machinery',ch19:'Operation & Maint.',ch20:'Fire Safety',ch21:'LPG Safety',ch22:'Environmental'
    },
    partA: 'Part A (ch1-ch13)', partB: 'Part B (ch14-ch22)',
    infoHtml: `<h3>📋 Exam Rules</h3><ul>
      <li><b>Part A (Navigation/Safety)</b>: 40 MCQs, 45 min, 60% to pass</li>
      <li><b>Part B (Engineering)</b>: 40 MCQs, 45 min, 60% to pass</li>
      <li>Parts scored independently; passing grade retained for 2 years</li>
      <li>Computer-based examination</li>
    </ul><h3 style="margin-top:16px">📝 Registration</h3><ul>
      <li>Provider: <a href="https://www.peak.edu.hk" target="_blank">PEAK Institute</a></li>
      <li>Tel: 2836 0000</li>
    </ul><h3 style="margin-top:16px">📚 Syllabus</h3><ul>
      <li><b>Part A</b>: Vessel handling, anchoring, safety, chart work, tides, visibility, local knowledge, COLREGS, safety equipment, VHF, Marine Dept, weather, emergencies</li>
      <li><b>Part B</b>: IC engine principles, petrol/diesel/outboard engines, auxiliaries, maintenance, fire safety, LPG safety, environmental protection</li>
    </ul>`
  }
};

/* ========== STATE ========== */
let lang = localStorage.getItem('pvoc_lang') || 'zh-CN';
let theme = localStorage.getItem('pvoc_theme') || 'light';
let mode = ''; // 'practice', 'examA', 'examB'
let currentQs = [];
let currentIdx = 0;
let answers = {}; // qid -> selected option index
let examTimer = null;
let examTimeLeft = 0;
let wrongIds = JSON.parse(localStorage.getItem('pvoc_wrong') || '[]');
let doneMap = JSON.parse(localStorage.getItem('pvoc_done') || '{}'); // qid -> {correct: bool}

/* ========== HELPERS ========== */
function t(key) { return (UI[lang] || UI['zh-CN'])[key] || key; }
function chName(ch) { return t('chNames')[ch] || ch; }
function qText(q) { return q.q[lang] || q.q['zh-CN'] || q.q['en'] || ''; }
function oText(q, i) { const o = q.o[i]; return o ? (o[lang] || o['zh-CN'] || o['en'] || '') : ''; }
function expText(q) { return q.exp[lang] || q.exp['zh-CN'] || q.exp['en'] || ''; }
function letter(i) { return ['A','B','C','D'][i]; }

function saveState() {
  localStorage.setItem('pvoc_lang', lang);
  localStorage.setItem('pvoc_theme', theme);
  localStorage.setItem('pvoc_wrong', JSON.stringify(wrongIds));
  localStorage.setItem('pvoc_done', JSON.stringify(doneMap));
}

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/* ========== THEME ========== */
function applyTheme() {
  document.documentElement.setAttribute('data-theme', theme);
  document.getElementById('themeBtn').textContent = theme === 'dark' ? '☀️' : '🌙';
}
function toggleTheme() {
  theme = theme === 'dark' ? 'light' : 'dark';
  applyTheme();
  saveState();
}

/* ========== LANGUAGE ========== */
function setLang(l) {
  lang = l;
  document.documentElement.lang = l === 'zh-CN' ? 'zh-CN' : l === 'zh-TW' ? 'zh-TW' : 'en';
  document.querySelectorAll('.lang-btn').forEach(b => b.classList.toggle('active', b.dataset.lang === l));
  saveState();
  updateUI();
  // Re-render current page
  const activePage = document.querySelector('.page.active');
  if (activePage) {
    if (activePage.id === 'menuPage') showMenu();
    else if (activePage.id === 'chapterPage') showChapters();
    else if (activePage.id === 'questionPage') renderQuestion();
    else if (activePage.id === 'resultPage') renderResult();
    else if (activePage.id === 'wrongPage') showWrong();
    else if (activePage.id === 'infoPage') showInfo();
  }
}

function updateUI() {
  document.getElementById('pageTitle').textContent = t('title');
  document.getElementById('tPractice').textContent = t('practice');
  document.getElementById('tPracticeD').textContent = t('practiceD');
  document.getElementById('tExamA').textContent = t('examA');
  document.getElementById('tExamAD').textContent = t('examAD');
  document.getElementById('tExamB').textContent = t('examB');
  document.getElementById('tExamBD').textContent = t('examBD');
  document.getElementById('tInfo').textContent = t('info');
  document.getElementById('tInfoD').textContent = t('infoD');
  document.getElementById('tWrong').textContent = t('wrong');
  document.getElementById('tWrongD').textContent = t('wrongD');
  document.getElementById('tChTitle').textContent = t('chTitle');
  document.getElementById('tBack1').textContent = t('back');
  document.getElementById('tBack2').textContent = t('back');
  document.getElementById('tBack3').textContent = t('back');
  document.getElementById('btnPrev').textContent = t('prev');
  document.getElementById('btnNext').textContent = t('next');
  document.getElementById('expLabel').textContent = t('expLabel');
  document.getElementById('tReview').textContent = t('review');
  document.getElementById('tWrongTitle').textContent = t('wrongTitle');
  updateStats();
}

function updateStats() {
  const total = ALL_Q.length;
  const done = Object.keys(doneMap).length;
  const correct = Object.values(doneMap).filter(d => d.correct).length;
  document.getElementById('statsBar').innerHTML =
    `<span>${t('totalQ')}: ${total}</span><span>${t('doneQ')}: ${done}</span><span>${t('correctQ')}: ${correct}</span>`;
  const pct = total > 0 ? Math.round(done / total * 100) : 0;
  document.getElementById('progressFill').style.width = pct + '%';
}

/* ========== NAVIGATION ========== */
function showPage(id) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  window.scrollTo(0, 0);
}

function showMenu() {
  stopTimer();
  mode = '';
  currentQs = [];
  currentIdx = 0;
  answers = {};
  showPage('menuPage');
  updateUI();
}

/* ========== CHAPTERS ========== */
function startPractice() {
  mode = 'practice';
  answers = {};
  showChapters();
}

function showChapters() {
  showPage('chapterPage');
  const isPartA = true; // show all chapters
  const chMap = {};
  ALL_Q.forEach(q => {
    if (!chMap[q.ch]) chMap[q.ch] = {total: 0, done: 0, correct: 0};
    chMap[q.ch].total++;
    if (doneMap[q.id]) {
      chMap[q.ch].done++;
      if (doneMap[q.ch]) chMap[q.ch].correct++;
    }
  });
  const chOrder = ['ch1','ch2','ch3','ch4','ch5','ch6','ch7','ch8','ch9','ch10','ch11','ch12','ch13',
                    'ch14','ch15','ch16','ch17','ch18','ch19','ch20','ch21','ch22'];
  let html = `<div class="ch-card" onclick="startChapter('all')" style="border-color:var(--warn)">
    <div><div class="ch-name">${lang==='en'?'All Chapters':'全部章节'}</div>
    <div class="ch-desc">${lang==='en'?`${ALL_Q.length} questions`:`${ALL_Q.length} 题`}</div></div>
    <div class="ch-count">${ALL_Q.length}</div></div>`;

  // Part A section
  html += `<div style="margin-top:12px;font-size:13px;font-weight:700;color:var(--danger)">${t('partA')}</div>`;
  for (const ch of chOrder.slice(0, 13)) {
    if (!chMap[ch]) continue;
    const d = chMap[ch];
    html += `<div class="ch-card" onclick="startChapter('${ch}')">
      <div><div class="ch-name">${chName(ch)}</div>
      <div class="ch-progress">${d.done}/${d.total} ${lang==='en'?'done':'已完成'}</div></div>
      <div class="ch-count">${d.total}</div></div>`;
  }

  // Part B section
  html += `<div style="margin-top:12px;font-size:13px;font-weight:700;color:#8e44ad">${t('partB')}</div>`;
  for (const ch of chOrder.slice(13)) {
    if (!chMap[ch]) continue;
    const d = chMap[ch];
    html += `<div class="ch-card" onclick="startChapter('${ch}')">
      <div><div class="ch-name">${chName(ch)}</div>
      <div class="ch-progress">${d.done}/${d.total} ${lang==='en'?'done':'已完成'}</div></div>
      <div class="ch-count">${d.total}</div></div>`;
  }
  document.getElementById('chapterList').innerHTML = html;
}

function startChapter(ch) {
  currentQs = ch === 'all' ? [...ALL_Q] : ALL_Q.filter(q => q.ch === ch);
  currentIdx = 0;
  answers = {};
  showPage('questionPage');
  renderQuestion();
}

/* ========== EXAM MODE ========== */
function startExamA() {
  mode = 'examA';
  const partA = ALL_Q.filter(q => {
    const cn = parseInt(q.ch.replace('ch',''));
    return cn >= 1 && cn <= 13;
  });
  currentQs = shuffle(partA).slice(0, 40);
  currentIdx = 0;
  answers = {};
  startTimer(45 * 60);
  showPage('questionPage');
  renderQuestion();
}

function startExamB() {
  mode = 'examB';
  const partB = ALL_Q.filter(q => {
    const cn = parseInt(q.ch.replace('ch',''));
    return cn >= 14 && cn <= 22;
  });
  currentQs = shuffle(partB).slice(0, 40);
  currentIdx = 0;
  answers = {};
  startTimer(45 * 60);
  showPage('questionPage');
  renderQuestion();
}

/* ========== TIMER ========== */
function startTimer(seconds) {
  examTimeLeft = seconds;
  updateTimerDisplay();
  document.getElementById('timerBar').classList.add('show');
  examTimer = setInterval(() => {
    examTimeLeft--;
    updateTimerDisplay();
    if (examTimeLeft <= 0) {
      clearInterval(examTimer);
      examTimer = null;
      submitExam();
    }
  }, 1000);
}

function stopTimer() {
  if (examTimer) { clearInterval(examTimer); examTimer = null; }
  document.getElementById('timerBar').classList.remove('show');
}

function updateTimerDisplay() {
  const m = Math.floor(examTimeLeft / 60);
  const s = examTimeLeft % 60;
  const el = document.getElementById('timerDisplay');
  el.textContent = `${m}:${s.toString().padStart(2,'0')}`;
  el.parentElement.classList.toggle('timer-warn', examTimeLeft <= 300);
}

/* ========== QUESTIONS ========== */
function renderQuestion() {
  if (!currentQs.length) return;
  const q = currentQs[currentIdx];
  document.getElementById('qNum').textContent = currentIdx + 1;
  document.getElementById('qTotal').textContent = currentQs.length;
  document.getElementById('qChapter').textContent = chName(q.ch);
  document.getElementById('qText').textContent = qText(q);

  // Image
  const imgWrap = document.getElementById('qImgWrap');
  if (q.img) {
    document.getElementById('qImg').src = 'images/' + q.img;
    imgWrap.style.display = '';
  } else {
    imgWrap.style.display = 'none';
  }

  // Options
  const answered = answers[q.id] !== undefined;
  const optBox = document.getElementById('optBox');
  let optHtml = '';
  for (let i = 0; i < 4; i++) {
    let cls = 'option';
    if (answered) cls += ' locked';
    if (answered && answers[q.id] === i) {
      cls += i === q.a ? ' correct' : ' wrong';
    }
    if (answered && i === q.a) cls += ' correct';
    optHtml += `<div class="${cls}" onclick="selectOption(${i})">
      <span class="letter">${letter(i)}</span>
      <span>${oText(q, i)}</span>
    </div>`;
  }
  optBox.innerHTML = optHtml;

  // Explanation
  const expBox = document.getElementById('expBox');
  const exp = expText(q);
  if (answered && exp) {
    document.getElementById('expText').textContent = exp;
    expBox.classList.add('show');
  } else {
    expBox.classList.remove('show');
  }

  // Navigation
  document.getElementById('btnPrev').disabled = currentIdx === 0;
  const isLast = currentIdx === currentQs.length - 1;
  const btnNext = document.getElementById('btnNext');
  if (mode && isLast) {
    btnNext.textContent = t('submit');
    btnNext.onclick = submitExam;
  } else {
    btnNext.textContent = t('next');
    btnNext.onclick = nextQ;
  }
  btnNext.disabled = false;
}

function selectOption(i) {
  const q = currentQs[currentIdx];
  if (answers[q.id] !== undefined) return;
  answers[q.id] = i;
  const correct = i === q.a;
  doneMap[q.id] = {correct};
  if (!correct && !wrongIds.includes(q.id)) wrongIds.push(q.id);
  if (correct && wrongIds.includes(q.id)) wrongIds = wrongIds.filter(id => id !== q.id);
  saveState();
  renderQuestion();
}

function prevQ() {
  if (currentIdx > 0) { currentIdx--; renderQuestion(); }
}

function nextQ() {
  if (currentIdx < currentQs.length - 1) { currentIdx++; renderQuestion(); }
}

/* ========== RESULTS ========== */
function submitExam() {
  stopTimer();
  let correct = 0, wrong = 0;
  const wrongQs = [];
  currentQs.forEach(q => {
    const a = answers[q.id];
    if (a !== undefined) {
      if (a === q.a) correct++;
      else { wrong++; wrongQs.push(q); }
    } else { wrong++; wrongQs.push(q); }
  });
  const total = currentQs.length;
  const pct = Math.round(correct / total * 100);
  const pass = pct >= 60;

  document.getElementById('resTitle').textContent = mode === 'examA' ? t('examA') : mode === 'examB' ? t('examB') : t('practice');
  const scoreEl = document.getElementById('resScore');
  scoreEl.textContent = pct + '%';
  scoreEl.className = 'result-score ' + (pass ? 'pass' : 'fail');
  document.getElementById('resBarFill').style.width = pct + '%';
  document.getElementById('resBarFill').style.background = pass ? 'var(--success)' : 'var(--danger)';
  document.getElementById('resMsg').textContent = pass ? t('passMsg') : t('failMsg');
  document.getElementById('resCorrect').textContent = correct;
  document.getElementById('resWrong').textContent = wrong;

  // Review list
  let revHtml = '';
  wrongQs.forEach((q, idx) => {
    revHtml += `<div class="review-item" onclick="reviewQ('${q.id}')">
      <div class="ri-num">${lang==='en'?'Q':'第'}${idx+1}${lang==='en'?'':'题'} | ${chName(q.ch)}</div>
      <div class="ri-text">${qText(q).substring(0, 80)}...</div>
      <div class="ri-ans" style="color:var(--danger)">${lang==='en'?'Your':'你的'}: ${letter(answers[q.id]||0)} | ${lang==='en'?'Correct':'正确'}: ${letter(q.a)}</div>
    </div>`;
  });
  document.getElementById('reviewList').innerHTML = revHtml || `<div class="empty-msg">${lang==='en'?'All correct!':'全部答对！'}</div>`;

  showPage('resultPage');
  window.scrollTo(0, 0);
}

function reviewQ(qid) {
  const idx = currentQs.findIndex(q => q.id === qid);
  if (idx >= 0) {
    currentIdx = idx;
    showPage('questionPage');
    renderQuestion();
  }
}

function retryWrong() {
  const wq = currentQs.filter(q => wrongIds.includes(q.id));
  if (!wq.length) { showMenu(); return; }
  currentQs = shuffle(wq);
  currentIdx = 0;
  answers = {};
  mode = 'practice';
  showPage('questionPage');
  renderQuestion();
}

/* ========== WRONG ANSWERS PAGE ========== */
function showWrong() {
  showPage('wrongPage');
  document.getElementById('wrongCount').textContent =
    `${lang==='en'?'Total wrong':'错题总数'}: ${wrongIds.length}`;
  let html = '';
  wrongIds.forEach((qid, idx) => {
    const q = ALL_Q.find(x => x.id === qid);
    if (!q) return;
    html += `<div class="review-item" onclick="reviewWrongQ('${qid}')">
      <div class="ri-num">${idx+1} | ${chName(q.ch)}</div>
      <div class="ri-text">${qText(q).substring(0, 80)}...</div>
    </div>`;
  });
  document.getElementById('wrongList').innerHTML = html || `<div class="empty-msg">${t('emptyWrong')}</div>`;
}

function reviewWrongQ(qid) {
  const q = ALL_Q.find(x => x.id === qid);
  if (!q) return;
  mode = 'practice';
  currentQs = [q];
  currentIdx = 0;
  answers = {};
  showPage('questionPage');
  renderQuestion();
}

/* ========== INFO PAGE ========== */
function showInfo() {
  showPage('infoPage');
  document.getElementById('infoContent').innerHTML = t('infoHtml');
}

/* ========== INIT ========== */
function init() {
  applyTheme();
  document.querySelectorAll('.lang-btn').forEach(b => b.classList.toggle('active', b.dataset.lang === lang));
  updateUI();
  showMenu();
}

init();
</script>
</body>
</html>'''

def main():
    print("Building index.html...")
    questions = build_questions()
    print(f"  Loaded {len(questions)} questions")

    # Serialize questions
    q_json = json.dumps(questions, ensure_ascii=False, separators=(',', ':'))

    # Serialize T2S map
    t2s_json = json.dumps(T2S, ensure_ascii=False, separators=(',', ':'))

    # Build HTML
    html = HTML_TEMPLATE.replace('__QUESTIONS_JSON__', q_json).replace('__T2S_JSON__', t2s_json)

    out_path = os.path.join(BASE, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Written to {out_path} ({len(html)} bytes)")
    print("Done!")

if __name__ == '__main__':
    main()
