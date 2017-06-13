

#Author: Navjot Singh Babrah
from selenium import webdriver
from instagram.client import InstagramAPI
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time,sched
import sched
s = sched.scheduler(time.time, time.sleep)
username = "jeffrr111111"
password = "jeff1234"
target='gagan_babrah_7860'
target1='jeffrr111111'
# time.sleep(3)


PROXY = "127.0.0.1:34005" # IP:PORT or HOST:PORT
PROXY1 = "127.0.0.1:34002" # IP:PORT or HOST:PORT
PROXY2 = "127.0.0.1:34003" # IP:PORT or HOST:PORT

paid_user=['jonathananthan','davidryan0']
password=['tigerisback','therockiscooking']
proxy=['127.0.0.1:34002','127.0.0.1:34003','127.0.0.1:34002','127.0.0.1:34002','127.0.0.1:34003']

# target=['manpreetsingh8750','bennuttan','samra1850','pavitar_chhina_','deep3214']
target=['gagan_babrah_7860',
'luxuryrumor',
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
'visionary_goals',
]

i=0
# d=0
p1=0
u1=0




# chrome_options.add_argument('--proxy-server=http://%s' % PROXY1)
#
#
# chrome = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"../../Downloads/chromedriver")

def userprofile_info(sc):
    for u,p,r,i in zip(paid_user,password,proxy,target):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=http://%s' % r)

        chrome = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"../../usr/local/bin/chromedriver")
        dd1 = ("https://www.instagram.com/accounts/login/")
        driver1 = chrome
        driver1.get(dd1)
        try:
            driver1.find_element_by_xpath("//input[@name='username']").send_keys("".join(str(u)))
            driver1.find_element_by_xpath("//input[@name='password']").send_keys("".join(str(p)))


            driver1.find_element_by_xpath("//button[contains(.,'Log in')]").click()

        except:
            continue

        print(p, u,r,i)
        d=0

        for i in target:
            print i

            if (d <=len(target)):
                url=  ("https://www.instagram.com/"+ "".join(str(i)))
                dd1 = url
                driver1 = chrome
                driver1.get(dd1)
                try:
                    driver1.find_element_by_css_selector('._ovg3g').click()
                    time.sleep(3)
                except:
                    continue

                try:
                    driver1.find_element_by_xpath("//span[contains(.,'Like')]").click()
                except:
                    driver1.find_element_by_css_selector('._3eajp').click()
                    print(driver1.get('https://lumtest.com/myip.json'))

                    # s.enter(6, 1, userprofile_info, (sc,))
            if(i[-2]):
                 try:
                   driver1.quit()
                 #   continue
                 except:
                     print 'err'
                 #   continue




                    # driver1.quit()

                # s.enter(6, 1, userprofile_info, (sc,))










  # time.sleep(4)
        # s.enter(6, 1, userprofile_info, (sc,))






                    # driver1.find_element_by_css_selector('._phrgb').click() for follow
                # time.sleep(3)
                # while True:
                #     try:
                #         print(driver1.get('https://lumtest.com/myip.json'))
                #         time.sleep(4)
                #         s.enter(6, 1, userprofile_info, (sc,))
                #
                #
                #     except:
                #         # driver1.find_element_by_css_selector('._3eajp').click()
                #         time.sleep(2)
                #         s.enter(6, 1, userprofile_info, (sc,))







                # driver1.find_element_by_css_selector('._soakw ._vbtk2 ').click()












s.enter(1, 1, userprofile_info, (s,))
# s.run()
s.run()
while True:
    try:
        s.run()
    except:
        print 'Error'
        continue



# d+=1
#







# https://www.instagram.com/jeffrr111111/?__a=1    use to get user info as url







# "x%d"%i = data[:,i-1]


# r=driver1.find_element_by_xpath("//div[@class='_a1rcs']").click()
# driver1.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target1)
# print params['o']
# wait = WebDriverWait(driver1, 20)
# driver1.find_element_linktext('/navjotbabrah/').click()  'gagan_babrah_7860','jeffrr111111','davinderbhullar_90',
