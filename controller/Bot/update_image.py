import urllib
import json
# import threading
import requests
# from flask import Flask
# import urllib.request
import time
from PIL import Image
# from StringIO import StringIO
import sched
s = sched.scheduler(time.time, time.sleep)
# proxy=['127.0.0.1:34003','127.0.0.1:34002','127.0.0.1:34003','127.0.0.1:34002','127.0.0.1:34002','127.0.0.1:34006','127.0.0.1:34007','127.0.0.1:34008','127.0.0.1:34009','127.0.0.1:34010','127.0.0.1:34002']
proxy=['http://127.0.0.1:34003','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34005','http://127.0.0.1:22225','http://127.0.0.1:34006','http://127.0.0.1:34007','http://127.0.0.1:34008','http://127.0.0.1:34009','http://127.0.0.1:34010','http://127.0.0.1:34011','http://127.0.0.1:22225','http://127.0.0.1:34002','http://127.0.0.1:34003','http://127.0.0.1:22225','http://127.0.0.1:34013','http://127.0.0.1:34014','http://127.0.0.1:34015','http://127.0.0.1:34016','http://127.0.0.1:22225','http://127.0.0.1:34017','http://127.0.0.1:34018','http://127.0.0.1:34019','http://127.0.0.1:34020','http://127.0.0.1:34021','http://127.0.0.1:34005','http://127.0.0.1:34031','http://127.0.0.1:34011','http://127.0.0.1:34010','http://127.0.0.1:34003','http://127.0.0.1:34008','http://127.0.0.1:22225','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34009','http://127.0.0.1:34007','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:34011','http://127.0.0.1:34024','http://127.0.0.1:34025','http://127.0.0.1:34026','http://127.0.0.1:34027','http://127.0.0.1:34028','http://127.0.0.1:34029','http://127.0.0.1:34030','http://127.0.0.1:34032','http://127.0.0.1:34033','http://127.0.0.1:34034','http://127.0.0.1:34035','http://127.0.0.1:34036','http://127.0.0.1:34037','http://127.0.0.1:34038','http://127.0.0.1:34030','http://127.0.0.1:34003','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34005','http://127.0.0.1:22225','http://127.0.0.1:34006','http://127.0.0.1:34007','http://127.0.0.1:34008','http://127.0.0.1:34009','http://127.0.0.1:34010','http://127.0.0.1:34011','http://127.0.0.1:22225','http://127.0.0.1:34002','http://127.0.0.1:34003','http://127.0.0.1:22225','http://127.0.0.1:34013','http://127.0.0.1:34014','http://127.0.0.1:34015','http://127.0.0.1:34016','http://127.0.0.1:22225','http://127.0.0.1:34017','http://127.0.0.1:34018','http://127.0.0.1:34019','http://127.0.0.1:34020','http://127.0.0.1:34021','http://127.0.0.1:34005','http://127.0.0.1:34031','http://127.0.0.1:34011','http://127.0.0.1:34010','http://127.0.0.1:34003','http://127.0.0.1:34008','http://127.0.0.1:22225','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34009','http://127.0.0.1:34007','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:34011','http://127.0.0.1:34024','http://127.0.0.1:34025','http://127.0.0.1:34026','http://127.0.0.1:34027','http://127.0.0.1:34028','http://127.0.0.1:34029','http://127.0.0.1:34030','http://127.0.0.1:34032','http://127.0.0.1:34033','http://127.0.0.1:34034','http://127.0.0.1:34035','http://127.0.0.1:34036','http://127.0.0.1:34037','http://127.0.0.1:34038','http://127.0.0.1:34030','http://127.0.0.1:34003','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34005','http://127.0.0.1:22225','http://127.0.0.1:34006','http://127.0.0.1:34007','http://127.0.0.1:34008','http://127.0.0.1:34009','http://127.0.0.1:34010','http://127.0.0.1:34011','http://127.0.0.1:22225','http://127.0.0.1:34002','http://127.0.0.1:34003','http://127.0.0.1:22225','http://127.0.0.1:34013','http://127.0.0.1:34014','http://127.0.0.1:34015','http://127.0.0.1:34016','http://127.0.0.1:22225','http://127.0.0.1:34017','http://127.0.0.1:34018','http://127.0.0.1:34019','http://127.0.0.1:34020','http://127.0.0.1:34021','http://127.0.0.1:34005','http://127.0.0.1:34031','http://127.0.0.1:34011','http://127.0.0.1:34010','http://127.0.0.1:34003','http://127.0.0.1:34008','http://127.0.0.1:22225','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34009','http://127.0.0.1:34007','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:34011','http://127.0.0.1:34024','http://127.0.0.1:34025','http://127.0.0.1:34026','http://127.0.0.1:34027','http://127.0.0.1:34028','http://127.0.0.1:34029','http://127.0.0.1:34030','http://127.0.0.1:34032','http://127.0.0.1:34033','http://127.0.0.1:34034','http://127.0.0.1:34035','http://127.0.0.1:34036','http://127.0.0.1:34037','http://127.0.0.1:34038','http://127.0.0.1:34030','http://127.0.0.1:34003','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34005','http://127.0.0.1:22225','http://127.0.0.1:34006','http://127.0.0.1:34007','http://127.0.0.1:34008','http://127.0.0.1:34009','http://127.0.0.1:34010','http://127.0.0.1:34011','http://127.0.0.1:22225','http://127.0.0.1:34002','http://127.0.0.1:34003','http://127.0.0.1:22225','http://127.0.0.1:34013','http://127.0.0.1:34014','http://127.0.0.1:34015','http://127.0.0.1:34016','http://127.0.0.1:22225','http://127.0.0.1:34017','http://127.0.0.1:34018','http://127.0.0.1:34019','http://127.0.0.1:34020','http://127.0.0.1:34021','http://127.0.0.1:34005','http://127.0.0.1:34031','http://127.0.0.1:34011','http://127.0.0.1:34010','http://127.0.0.1:34003','http://127.0.0.1:34008','http://127.0.0.1:22225','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34009','http://127.0.0.1:34007','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:34011','http://127.0.0.1:34024','http://127.0.0.1:34025','http://127.0.0.1:34026','http://127.0.0.1:34027','http://127.0.0.1:34028','http://127.0.0.1:34029','http://127.0.0.1:34030','http://127.0.0.1:34032','http://127.0.0.1:34033','http://127.0.0.1:34034','http://127.0.0.1:34035','http://127.0.0.1:34036','http://127.0.0.1:34037','http://127.0.0.1:34038','http://127.0.0.1:34030','http://127.0.0.1:34003','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34005','http://127.0.0.1:22225','http://127.0.0.1:34006','http://127.0.0.1:34007','http://127.0.0.1:34008','http://127.0.0.1:34009','http://127.0.0.1:34010','http://127.0.0.1:34011','http://127.0.0.1:22225','http://127.0.0.1:34002','http://127.0.0.1:34003','http://127.0.0.1:22225','http://127.0.0.1:34013','http://127.0.0.1:34014','http://127.0.0.1:34015','http://127.0.0.1:34016','http://127.0.0.1:22225','http://127.0.0.1:34017','http://127.0.0.1:34018','http://127.0.0.1:34019','http://127.0.0.1:34020','http://127.0.0.1:34021','http://127.0.0.1:34005','http://127.0.0.1:34031','http://127.0.0.1:34011','http://127.0.0.1:34010','http://127.0.0.1:34003','http://127.0.0.1:34008','http://127.0.0.1:22225','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34009','http://127.0.0.1:34007','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:34011','http://127.0.0.1:34024','http://127.0.0.1:34025','http://127.0.0.1:34026','http://127.0.0.1:34027','http://127.0.0.1:34028','http://127.0.0.1:34029','http://127.0.0.1:34030','http://127.0.0.1:34032','http://127.0.0.1:34033','http://127.0.0.1:34034','http://127.0.0.1:34035','http://127.0.0.1:34036','http://127.0.0.1:34037','http://127.0.0.1:34038','http://127.0.0.1:34030','http://127.0.0.1:34003','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34005','http://127.0.0.1:22225','http://127.0.0.1:34006','http://127.0.0.1:34007','http://127.0.0.1:34008','http://127.0.0.1:34009','http://127.0.0.1:34010','http://127.0.0.1:34011','http://127.0.0.1:22225','http://127.0.0.1:34002','http://127.0.0.1:34003','http://127.0.0.1:22225','http://127.0.0.1:34013','http://127.0.0.1:34014','http://127.0.0.1:34015','http://127.0.0.1:34016','http://127.0.0.1:22225','http://127.0.0.1:34017','http://127.0.0.1:34018','http://127.0.0.1:34019','http://127.0.0.1:34020','http://127.0.0.1:34021','http://127.0.0.1:34005','http://127.0.0.1:34031','http://127.0.0.1:34011','http://127.0.0.1:34010','http://127.0.0.1:34003','http://127.0.0.1:34008','http://127.0.0.1:22225','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34009','http://127.0.0.1:34007','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:34011','http://127.0.0.1:34024','http://127.0.0.1:34025','http://127.0.0.1:34026','http://127.0.0.1:34027','http://127.0.0.1:34028','http://127.0.0.1:34029','http://127.0.0.1:34030','http://127.0.0.1:34032','http://127.0.0.1:34033','http://127.0.0.1:34034','http://127.0.0.1:34035','http://127.0.0.1:34036','http://127.0.0.1:34037','http://127.0.0.1:34038','http://127.0.0.1:34030','http://127.0.0.1:34003','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34005','http://127.0.0.1:22225','http://127.0.0.1:34006','http://127.0.0.1:34007','http://127.0.0.1:34008','http://127.0.0.1:34009','http://127.0.0.1:34010','http://127.0.0.1:34011','http://127.0.0.1:22225','http://127.0.0.1:34002','http://127.0.0.1:34003','http://127.0.0.1:22225','http://127.0.0.1:34013','http://127.0.0.1:34014','http://127.0.0.1:34015','http://127.0.0.1:34016','http://127.0.0.1:22225','http://127.0.0.1:34017','http://127.0.0.1:34018','http://127.0.0.1:34019','http://127.0.0.1:34020','http://127.0.0.1:34021','http://127.0.0.1:34005','http://127.0.0.1:34031','http://127.0.0.1:34011','http://127.0.0.1:34010','http://127.0.0.1:34003','http://127.0.0.1:34008','http://127.0.0.1:22225','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34009','http://127.0.0.1:34007','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:34011','http://127.0.0.1:34024','http://127.0.0.1:34025','http://127.0.0.1:34026','http://127.0.0.1:34027','http://127.0.0.1:34028','http://127.0.0.1:34029','http://127.0.0.1:34030','http://127.0.0.1:34032','http://127.0.0.1:34033','http://127.0.0.1:34034','http://127.0.0.1:34035','http://127.0.0.1:34036','http://127.0.0.1:34037','http://127.0.0.1:34038','http://127.0.0.1:34030','http://127.0.0.1:34003','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34005','http://127.0.0.1:22225','http://127.0.0.1:34006','http://127.0.0.1:34007','http://127.0.0.1:34008','http://127.0.0.1:34009','http://127.0.0.1:34010','http://127.0.0.1:34011','http://127.0.0.1:22225','http://127.0.0.1:34002','http://127.0.0.1:34003','http://127.0.0.1:22225','http://127.0.0.1:34013','http://127.0.0.1:34014','http://127.0.0.1:34015','http://127.0.0.1:34016','http://127.0.0.1:22225','http://127.0.0.1:34017','http://127.0.0.1:34018','http://127.0.0.1:34019','http://127.0.0.1:34020','http://127.0.0.1:34021','http://127.0.0.1:34005','http://127.0.0.1:34031','http://127.0.0.1:34011','http://127.0.0.1:34010','http://127.0.0.1:34003','http://127.0.0.1:34008','http://127.0.0.1:22225','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34009','http://127.0.0.1:34007','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:34011','http://127.0.0.1:34024','http://127.0.0.1:34025','http://127.0.0.1:34026','http://127.0.0.1:34027','http://127.0.0.1:34028','http://127.0.0.1:34029','http://127.0.0.1:34030','http://127.0.0.1:34032','http://127.0.0.1:34033','http://127.0.0.1:34034','http://127.0.0.1:34035','http://127.0.0.1:34036','http://127.0.0.1:34037','http://127.0.0.1:34038','http://127.0.0.1:34030','http://127.0.0.1:34003','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34005','http://127.0.0.1:22225','http://127.0.0.1:34006','http://127.0.0.1:34007','http://127.0.0.1:34008','http://127.0.0.1:34009','http://127.0.0.1:34010','http://127.0.0.1:34011','http://127.0.0.1:22225','http://127.0.0.1:34002','http://127.0.0.1:34003','http://127.0.0.1:22225','http://127.0.0.1:34013','http://127.0.0.1:34014','http://127.0.0.1:34015','http://127.0.0.1:34016','http://127.0.0.1:22225','http://127.0.0.1:34017','http://127.0.0.1:34018','http://127.0.0.1:34019','http://127.0.0.1:34020','http://127.0.0.1:34021','http://127.0.0.1:34005','http://127.0.0.1:34031','http://127.0.0.1:34011','http://127.0.0.1:34010','http://127.0.0.1:34003','http://127.0.0.1:34008','http://127.0.0.1:22225','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34009','http://127.0.0.1:34007','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:34011','http://127.0.0.1:34024','http://127.0.0.1:34025','http://127.0.0.1:34026','http://127.0.0.1:34027','http://127.0.0.1:34028','http://127.0.0.1:34029','http://127.0.0.1:34030','http://127.0.0.1:34032','http://127.0.0.1:34033','http://127.0.0.1:34034','http://127.0.0.1:34035','http://127.0.0.1:34036','http://127.0.0.1:34037','http://127.0.0.1:34038','http://127.0.0.1:34030''http://127.0.0.1:34003','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34005','http://127.0.0.1:22225','http://127.0.0.1:34006','http://127.0.0.1:34007','http://127.0.0.1:34008','http://127.0.0.1:34009','http://127.0.0.1:34010','http://127.0.0.1:34011','http://127.0.0.1:22225','http://127.0.0.1:34002','http://127.0.0.1:34003','http://127.0.0.1:22225','http://127.0.0.1:34013','http://127.0.0.1:34014','http://127.0.0.1:34015','http://127.0.0.1:34016','http://127.0.0.1:22225','http://127.0.0.1:34017','http://127.0.0.1:34018','http://127.0.0.1:34019','http://127.0.0.1:34020','http://127.0.0.1:34021','http://127.0.0.1:34005','http://127.0.0.1:34031','http://127.0.0.1:34011','http://127.0.0.1:34010','http://127.0.0.1:34003','http://127.0.0.1:34008','http://127.0.0.1:22225','http://127.0.0.1:22225','http://127.0.0.1:24000','http://127.0.0.1:34009','http://127.0.0.1:34007','http://127.0.0.1:34002','http://127.0.0.1:22225','http://127.0.0.1:34011','http://127.0.0.1:34024','http://127.0.0.1:34025','http://127.0.0.1:34026','http://127.0.0.1:34027','http://127.0.0.1:34028','http://127.0.0.1:34029','http://127.0.0.1:34030','http://127.0.0.1:34032','http://127.0.0.1:34033','http://127.0.0.1:34034','http://127.0.0.1:34035','http://127.0.0.1:34036','http://127.0.0.1:34037','http://127.0.0.1:34038','http://127.0.0.1:34030']

boostlikes_users=['gagan_babrah_7860',

'Tunerlab',
'Bmwm_insta',
'Gojko.lojpur',
'jerseychampsllc',
'thedapperhaus',
'quotes4abundance',
'jae.sohn',
'anguilla_tourism',
'ashleighkwong',
'joergzuber',
'fashionambit',
'billionairemanifesto',
'_worldwidestance_',
'mastermindteam',
'eddiefitot',
'trxblackranks',
'being.charles',
'thezelatakogan',
'elevatedsociety',
'exploreresorts',
'transformationpost',
'allthisfood',
'healthyamazingrecipes',
'healthinspirationforyou',
'Kruetv',
'vendettaluxury',
'hotdogcartstore',
'product_sniper',
'Doublex',
'Luxeluce00',
'Millionaire.Aspiration',
'hard2findonline',
'masterocasio',
'wristrockers',
'ultimatetravellife',
'ultimatebossladies',
'mgvrd',
'alphaties',
'suitbible',
'qulturedclo',
'julejewellery',
'evanluthra',
'bottlepop_app',
'lisardovivas',
'millionaire.post',
'mums_guide',
'this_is_cardiff',
'440ent',
'styletomes',
'earths_hotspot',
'travellers_destiny',
'Guidetotravel',
'flylikewev',
'jeliaye',
'mrmhz',
'javierollero',
'Thinksmartgrowrichv',
'phillord.ca',
'big_dog_sean',
'explorer',
'mauricetravelphotos',
'nature.wish',
'travelersplacemagazine',
'onlyfortravel',
'Ontop.lifestyle',
'billionairemovements',
'Surelymine',
'successinventor',
'theluxuriousguy',
'fvckyourcomfortzonev',
'adore_world',
'flawlessmilano',
'flaviaarditi',
'Nikostraveler',
'scrumm.y',
'approved.booty',
'JesseniaVicev',
'topdailytravel',
'bodyburn',
'elationfitnessv',
'mr.highclass.co',
'itsjosuepena',
'joshforti',
'travelersmagazine',
'elationfootball',
'focus_mentality',
'travelest',
'luxrulebookv',
'dailyforti',
'travelbug',
'digitalceos',
'cocktailsgram',
'luxuries.magazine',
'elationathletics',
'futspotclub',
'dollars_mentality',
'svnetics',
'elationmoves',
'elationbasketball',
'inspiracion',
'ginicanbreathe',
'businessrulebook',
'_sevenkey_',
'itsbobbybooth',
'bestquotesinmylife',
'firstclass.vehicles',
'seventhirty.cars',
'travel_24seven',
'seventhirty.travel',
'firstclass.luxuries',
'seventhirty.luxury',
'gentlemankeys',
'fatloss_inspiration',
'pets.hub',
'fashillions',
'juniorentrepreneurs',
'nationsupercars',
'luxcargram',
'cars_globe_',
'lambo_nfs',
'mc_lambo',
'fatburner_females',
'gymgirls.ig',
'fit.chicks.only',
'fitness.girls.page',
'fitness_booties',
'motivate_urmind',
'motivated_strength',
'honorable_motivation',
'motivate_you_quotes',
'inspired_mindsets',
'motivated_grinder',
'motivated_preneur',
'firstclass_mindset',
'travelmatepage',
'dreamy_traveller',
'travelbuddypage',
'earthly_traveller',
'travellers_hotspot',
'travellers_favespots',
'traveller_hotspot',
'favespot_travels',
'vacation.hotspot',
'lovely_travelplaces',
'mrniksharma',
'kara.goldin',
'hint',
'nickshadlich',
'luxadvising',
'millennial_coach',
'lifeplaces',
'reallifetour',
'multibillionairemafia',
'elitemafia7',
'joyfulmillionaire',
'tuning_low_family',
'travelersofterra',
'airianagraande',
'highclassfastcars_',
'lixurysunfarm',
'warren__brown',
'r_white12',
'baseballrevelation',
'DavidAguwa',
'landrco',
'hackers_learn',
'digitalmoneylifestyle',
'bosslifenow',
'sticks_for_stones',
'giovannawheels',
'funny.mouth',
'_deluxevenue_',
'squirrels_wuirreld',
'loveforluxuries',
'_travelmuse_',
'commandmentsofstyle',
'whenindoubtblog',
'gameoverdosecom',
'pipmegan',
'millionaireaccess',
'the.elitemillionaire',
'Liveandgrowinla',
'watchfashionbible',
'vscrewcalories',
'vstonerhustle',
'luxurysunfarm',
'robinprediger',
'annesportun',
'ctlleather',
'vitamatcha',
'wayofwilldotcom',
'_arthirsch_',
'_rags_2_riches_',
'Greatlifenate',
'flavortips',
'tatianazoea',
'WikiBabies',
'gingerproblems',
'pet.zone.ig',
'richlivings',
'Beakinis',
'wearethisworld',
'aveniksmm',
'feelslikewealth',
'merieig',
'mytravel.passion',
'luxurious_success',
'lucapierr',
'successobsession',
'millionairesfocus',
'schiller.fitness',
'danfleyshman',
'adambravin',
'livingsuccesslifestyle',
'thepowerfulmindset',
'thestyleofus',
'fashiclassy',
'Ceomillionaire',
'mensweartutorial',
'billionairemasteryclub',
'millionrise',
'lux_proz',
'thatamazingfeed',
'billionaiire_lyfe',
'ilguarina',
'luxemaster',
'mstr_martian',
'richlivingz',
'lorenzomaddalena',
'billionaire_entourage',
'faithbaby',
'francesca.licchelli',
'millionairesafe',
'carhustlers',
'mindingherbusiness',
'familygoalz',
'honda_mafia',
'travel.at',
'iam.millionaire',
'_basik_',
'luxury_motivation365',
'socalbeachfit',
'millionaire.jets',
'dama_negra',
'anothermel',
'ruskothebostonterrier',
'money',
'eyeontheworld_official',
'psn',
'rossanavanoni',
'classymentor',
'seattle_mustang',
'anatakk',
'millionaire.academy',
'deluxelives',
'hero.burgers.montreal',
'a.dog.world',
'explore.our.globe',
'toptravelers',
'hollywoodbakedgoods',
'cocktail.video',
'ericjess',
'luxuriesmagazine',
'thebillionnet',
'glotrition',
'weliketosweat',
'WORLDOFBOSSES',
'workwithonel',
'ariencilla',
'social.ray',
'eyeshadowvideos',
'luxurygenii',
'fashionsfv',
'linneatheo_wbffpro',
'Success_Matrix',
'cleanestluxury',
'stellar_paradise',
'theluxfeed',
'millionaire.travels',
'vercettisr',
'hustlehardallthetime',
'jay_effect',
'billionaire_magazines',
'_billionairetycoon_',
'dalahi_ortiz',
'houseaddictive',
'babyplanets',
'luxewish',
'millionaireinspor',
'ilarya1994',
'bluete_beachwear',
'fashionphotographydaily',
'passportforallcountries',
'voyager_life',
'lorenanderson.photography',
'MillionaireProz',
'hustleclass',
'grinders.ambition',
'manucasy',
'pawsvision',
'thebrilliantbillionaire',
'makinamericagreat',
'travelswithenry',
'lnsta_dogs',
'123wander',
'artist.videos',
'jackcanevali',
'superiorsuccess',
'gobucketlist',
'fabrizioaldobelfiore',
'danielvozn',
'nolitanhotel',
'worldsbestinbikes',
'dalahiortiz',
'liteluxury',
'chiaragiraldi98',
'mar_nna',
'luxuriousleader',
'creating.wealth.together',
'millionsvibe',
'looks4cooks',
'project_mindset',
'themoodoflife',
'shopadda',
'build.a.bar',
'hustleistheanswerv',
'houses',
'mastertheluxury',
'millionaireish',
'bonistallivalentina',
'beautyfleek',
'atsunamatsui',
'boysaddict',
'millionzking',
'uyltodayv',
'yasiralnukaly',
'luxillion',
'for.architects',
'fitfiveofficiAl',
'havendelicates',
'luxoticy',
'trent_silver',
'luxuryrule',
'danielbistaffa',
'kindervideos',
'thebrunettessecrets',
'creativitywithkay',
'thetraininsane',
'miami_nightlife_guide',
'attitude_of_beautiful',
'lisalassi77',
'deluxe365',
'zeus.ironbeard',
'_beautifulliving_',
'firstclassmob',
'_millionaire_madness_',
'siriana_nappa',
'poshclassymom',
'_dgtravel_',
'DOSE_OF_SUCCESS',
'__hustlersmotivation__',
'Wonderful_bucketlist',
'bestofmenwear',
'businessheadshots',
'millionaire.market',
'adailydoseofdog',
'axen.art',
'_billionaireempire_',
'californiacarz',
'justluxuryls',
'sommeruddesign',
'inspravel',
'sun.beauties',
'wewantedm',
'katerinaporta',
'viralminute',
'world_greg',
'masterthemoneygame',
'positivethinking101',
'noblackheads',
'idea2girls',
'andreacasta',
'drift.junkies',
'fittrainers',
'benhampton',
'travelllion',
'millionaire.dreamlife',
'millionaire.vrooms',
'bauliusa',
'hazeforward',
'87domenico',
'creativeluxuries_',
'nature.unknown',
'housepitalgroup',
'insta.physiques',
'ivanovic95__',
'skyisthelimit_success',
'Luxwonder',
'thefrancimartin',
'jspeaks_',
'high.class.fashions',
'nutellavideo',
'thekingbrand',
'therichlifeteam',
'ladiesinluxe',
'visuallytasty',
'luxury_existence365',
'marikablonda',
'themotivationalperspective',
'oldschoolshots',
'millionairemasteryclub',
'millionsposts',
'lifestyledail.y',
'luigi_tuzzolino',
'boxepassion_',
'hallofbillionaires',
'rosario_vitale',
'247fitnessxxl',
'alessiomala98',
'elite_locations',
'husnainmalix',
'millionaire.gains',
'topstylez',
'bfr_bands',
'winepenguins',
'rohan_sheth',
'callmegaviin',
'featured_physiques',
'ichvse',
'licensed_to_distill',
'millionation',
'DallasBaldri',
'lihabonfio',
'motivillions',
'scensiblesbags',
'miglietta_lara',
'_armedforcespics_',
'luxdrift',
'visionary_goals'
]

# print proxy

d=0
def userprofile_info(sc):
    for i,r in zip(boostlikes_users,proxy):
        # print r
        # link=("https://www.instagram.com/"+"".join(str(i))+"/?__a=1")
        # # link = "https://www.instagram.com/gagan_babrah_7860/?__a=1"
        # f = urllib.urlopen(link)
        # myfile = f.read()
        #
        # data = json.loads(myfile)
        try:
            link=requests.get("http://www.instagram.com/"+"".join(str(i))+"/?__a=1" ,proxies={'http':''.join(str(r))})
            link1=requests.get("http://lumtest.com/myip.json" ,proxies={'http':''.join(str(r))})
            data=json.loads(link.content)
            data1=json.loads(link1.content)
            print (data['user']['username'])
            # # print (data['user']['post']['count'])
            # print (data['user']['biography'])
            # print (data['user']['follows']['count'])
            # print (data['user']['followed_by']['count'])
            # print (data['user']['profile_pic_url'])
            r=data['user']['media']['nodes']
            # print r
            # for u in r:
            #     print u['likes']['count']
            if len(r) < 1:
                print  (0)
                continue
            else:
                print r[0]['likes']['count']


        # need to change thread time 3 time per day
            print ("Updateing AutoRound!")
            # urllib.urlretrieve(''.join(data['user']['profile_pic_url']),"user_info/profile_img/tag/"+"".join(str(i))+".jpg")
            r = requests.get(''.join(data['user']['profile_pic_url']))
            # i = Image.open(StringIO(r.content))
            if r.status_code == 200:
                with open("user_info/profile_img/imge/"+''.join(data['user']['username'])+".jpg", 'wb') as f:
                    f.write(r.content)
                    # continue
                    # s.enter(5, 1, userprofile_info, (sc,))




        except:
            continue
            print data1

        # link = "https://www.instagram.com/gagan_babrah_7860/?__a=1"
        # f = requests.get(link,proxies={'http': 'http://10.11.4.254:3128'})



s.enter(1, 1, userprofile_info, (s,))
while True:
    try:
        s.run()
    except:
        print 'Error'
        continue


    # # params = urllib.urlencode(post_params)
