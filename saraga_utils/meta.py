from compmusic.dunya import hindustani as hi
from compmusic.dunya import carnatic as ca
import pandas as pd
import os

carnatic_cc = dict(tradition_id='a163c8f2-b75f-4655-86be-1504ea2944c2',
                    tradition_name='carnatic',
                    tradition_slug='dunya-carnatic-cc',
                    tradition_dunya=ca)
hindustani_cc = dict(tradition_id='6adc54c6-6605-4e57-8230-b85f1de5be2b',
                    tradition_name='hindustani',
                    tradition_slug='dunya-carnatic-cc',
                    tradition_dunya=hi)

info = {}
info['dunya-carnatic-cc'] = carnatic_cc
info['dunya-hindustani-cc'] = hindustani_cc

concept_mapp = {}
concert = 'release'
work = 'works'
raga = 'raags'
tala = 'taals'
form = 'forms'
laya = 'layas'
lead_artists = 'album_artists'
artists = 'artists'
entities = [concert, work, raga, tala, form, laya, artists, lead_artists, 'length']
id_mapping = {concert: 'mbid', work: 'mbid', raga: 'uuid', tala: 'uuid', form: 'name', laya: 'uuid',
              lead_artists: 'mbid', artists: 'mbid'}
concept_mapp['dunya-hindustani-cc'] = dict(entities=entities, id_mapping=id_mapping, release='release')

concert = 'concert'  # in carnatic album level items are referred by 'concerts'
work = 'work'
raga = 'raaga'
tala = 'taala'
form = 'form'
laya = 'laya'
lead_artists = 'album_artists'
artists = 'artists'
entities = [concert, work, raga, tala, form, laya, artists, lead_artists, 'length']
id_mapping = {concert: 'mbid', work: 'mbid', raga: 'uuid', tala: 'uuid', form: 'name', laya: 'uuid',
              lead_artists: 'mbid', artists: 'mbid'}
concept_mapp['dunya-carnatic-cc'] = dict(entities=entities, id_mapping=id_mapping, release='concert')

content_info_ca = pd.read_csv(os.path.join(os.path.dirname(__file__), 'carnatic_file_info.csv'))

content_info = {}
content_info['dunya-carnatic-cc'] = content_info_ca