
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documentos= [#lista de documentos
    'la casa es grande yt bontita',
    'el auto rojo esta en la calle ',
    'los arboles estan llenos de hojas',
    'el cielo azulse ve desde la ventana'
    ]

#consulta

consu = 'casa grande bonita'

#inicial el vectorizador tf-idf dy trasforma los documentos 

vector= TfidfVectorizer()
matriz= vector.fit_transform(documentos)

consu_vect= vector.transform([consu])
#calcula la similitud entre el documento y la consulta
similar = cosine_similarity(consu_vect,matriz)

#obtener indices de los documentos mas similares 

indice= similar.argsort()[0][::-1]

print('documentos similares a la consulta: ')
for idx in indice: 
    print(documentos[idx])