import streamlit as st
import json
import requests

with open('pokemon_index.json', 'r', encoding='utf-8')as arquivo:
    nomes_pokemon = json.load(arquivo)

nome = st.selectbox('Escolha um Pokemon', nomes_pokemon.values())

url = f'https://pokeapi.co/api/v2/pokemon/{nome}'

pokemon = requests.get(url).json()

col1, col2, col3 = st.columns(3)

with col1:
    st.image(pokemon['sprites']['front_default'], width=300)
    st.write('## Normal')

with col2:
    st.title(nome.capitalize())
    st.audio(pokemon['cries']['latest'])
    st.audio(pokemon['cries']['legacy'])

with col3:
    st.image(pokemon['sprites']['front_shiny'], width=300)
    st.write('## shiny')

col1, col2, col3 = st.columns(3)

altura = pokemon['height'] / 10 

peso = pokemon['weight'] / 10

imc = peso / (altura ** 2)

with col1:
    st.metric('altura', f'{altura} M')

with col2:
    st.metric('IMC', f'{imc:.2f}')

with col3:
    st.metric('peso', f'{peso} KG')

tipos, status, locais, habilidades = st.tabs(['Tipos', 'Status', 'Locais', 'Hablidades'])

with tipos:
    for tipo in pokemon['types']:
        st.markdown(f'- {tipo['type']['name']}')

with status:
    hp, ataque, defesa, ataque_esp, defesa_esp, velocidade = st.columns(6) 

    with hp:
        st.metric('HP', pokemon['stats'][0]['base_stat'])

    with ataque:
        st.metric('Ataque', pokemon['stats'][1]['base_stat'])

    with defesa:
        st.metric('Defesa', pokemon['stats'][2]['base_stat'])

    with ataque_esp:
        st.metric('ataque especial', pokemon['stats'][3]['base_stat'])

    with defesa_esp:
        st.metric('Defesa especial', pokemon['stats'][4]['base_stat'])

    with velocidade:
        st.metric('Velocidade', pokemon['stats'][5]['base_stat'])

with locais:
    locais = requests.get(pokemon['location_area_encounters']).json()
    for local in locais:
        st.markdown(f'- {local['location_area']['name']}') 

with habilidades:
    for habilidade in pokemon['abilities']:
        st.markdown(f'- {habilidade['ability']['name']}')


