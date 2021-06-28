import json
import os
import folium
import pandas as pd

m = folium.Map(location=[51.509865, -0.118092], zoom_start=11)
# vis = os.path.join('./data/clubsbytrophies.csv', 'vis.json')
overlay = os.path.join('data', 'london.json')

spurs_icon = folium.features.CustomIcon('./images/spurs.png', icon_size=(50,50))
brentford_icon = folium.features.CustomIcon('./images/brentford.png', icon_size=(50,50))
chelsea_icon = folium.features.CustomIcon('./images/chelsea.png', icon_size=(50,50))
palace_icon = folium.features.CustomIcon('./images/palace.png', icon_size=(50,50))
arsenal_icon = folium.features.CustomIcon('./images/arsenal.png', icon_size=(50,50))
westham_icon = folium.features.CustomIcon('./images/westham.png', icon_size=(50,50))

boroughs = os.path.join('data', 'london_sport.json')
trophies = os.path.join('data', 'clubsbytrophies.csv')
trophies_pd = pd.read_csv(trophies)



folium.Marker([51.604967, -0.072279], popup='<strong>White Hart Lane</strong><br> Tottenham have won 26 trophies', tooltip='Click for more',icon=spurs_icon).add_to(m)
folium.Marker([51.490825, -0.2887], popup='<strong>Brentford Community Stadium</strong><br> Brentford have never won a trophy', tooltip='Click for more',icon=brentford_icon).add_to(m)
folium.Marker([51.552997788, -0.105166246], popup='<strong>The Emirates</strong><br> Arsenal have 48 trophies', tooltip='Click for more',icon=arsenal_icon).add_to(m)
folium.Marker([51.475664764, -0.187999248], popup='<strong>Stamford Bridge</strong><br>Chelsea have 32 trophies', tooltip='Click for more',icon=chelsea_icon).add_to(m)
folium.Marker([51.536497854, -0.009833294], popup='<strong>London Stadium</strong><br> West Ham have won six trophies', tooltip='Click for more',icon=westham_icon).add_to(m)
folium.Marker([51.392331764, -0.084666328], popup='<strong>Selhurst Park</strong><br> Palace have won just one trophy', tooltip='Click for more',icon=palace_icon).add_to(m)


m.choropleth(
    geo_data=boroughs,
    name='chloropleth',
    data= trophies_pd,
    columns= ['Borough','Total'],
    key_on='properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity= 0.2,
    legend_name='Trophies by club'
)

folium.LayerControl().add_to(m)
# folium.Marker([51.509865, -0.118092], popup=folium.Popup(max_width=550).add_child(folium.Vega(json.load(open(vis))))).add_to(m)

folium.GeoJson(overlay, name='London').add_to(m)

m.save('LondonPremierLeague.html')

