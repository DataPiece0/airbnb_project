import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# setting the page's title, and logo
st.set_page_config(layout='wide',   page_icon='transparet logo.png', page_title='New York')

# telling dark mode users to switch to light mode for a  better view
aNoteForDarkModeUsers = '<p style="color:white">please use light mode for a better view</p>'
st.markdown(aNoteForDarkModeUsers, unsafe_allow_html=True)

# a header of the page
title='''<h1 style="color:black">AirBNB in New York</h1>'''
image1 = Image.open('airbnb.png')
st.markdown(title, unsafe_allow_html=True)
st.image(image1, width=200)
image2 = Image.open('logo_datapiece-removebg-preview.png')
st.image(image2, width=200)

descriptionOfProject ='''
<p style="color:black">
    Welcome to our project! in this project we will showcase our skills that we have obtained as students,
    we have made this project by getting a dataset about the AirBNB company from kaggle, this dataset is only set in New York in the Uinted States.
    After we got the dataset we cleaned it using Python in Jupyter Notebook, after that we used Tableau as a visualization tool to make our
    dashboard interactive, and finally we used streamlit as a way to write some of the html and host our project.
</p>
'''

descriptionOfAirBNB = '''
<p style="color:black">
    AirBNB is a company that specialize in in short-term and long-term homestays and experinces, the name AirBNB stands for Air, Bed and Breakfast
    reflecting the company’s humble beginnings when the founders rented out air mattresses in their apartment to attendees of a local conference.
    The company operates by connecting a host who has a accommodation to rent with a guest looking for a place to stay. Hosts list details about
    the accommodation, such as location, size, price, and availability, and guests can search for and book accommodations that meet their needs.
</p>
'''

mapLink = '''
<div class='tableauPlaceholder' id='viz1697512001131' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ma&#47;map_16975119825610&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='map_16975119825610&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ma&#47;map_16975119825610&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1697512001131');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height='651px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
'''

howToUseTheDashboard = '''
<p style="color:black">You can use the dashboard by chosing a neighbourhood group from the drop-down list, and then filter what kind of
BnBs you would like to see, you could for example pick the neighbourhood group Bronx and then filter the BnBs depending on the rating and cancellation
policy to see the names of BnBs that are suitable for your filtering.</p>
'''

st.write(''' # Description of the Project ''')
st.markdown(descriptionOfProject, unsafe_allow_html=True)
st.write(''' # What is AirBNB? ''')
st.markdown(descriptionOfAirBNB, unsafe_allow_html=True)
st.write(''' # Map of New York City and Its Neighbourhoods ''')
components.html(mapLink, height=600)
st.write(''' # How to Use the Dashboard? ''')
st.markdown(howToUseTheDashboard, unsafe_allow_html=True)


tableauLink = """
<div class='tableauPlaceholder' id='viz1697475590448' style='position: relative'><noscript><a href='#'><img alt='Dashboard 7 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;te&#47;test1_16972309187040&#47;Dashboard7&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='test1_16972309187040&#47;Dashboard7' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;te&#47;test1_16972309187040&#47;Dashboard7&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1697475590448');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='2077px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""
components.html(tableauLink, height=2100)

# details on how we have built the website
howWeDidIT ='''
        Thank you for checking our dashboard!
         now we will go through how we went on to create the dashboard from the bottom up!
         First of we uesd an open data set we found on kaggle made by Arian Azmoudeh from this <a href="https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata">link</a>,
         after that, we placed the data in a jupyter notebook to do the cleaning and the preprocessing part with Python,
         and then after we did that, we stored the data in PostgreSQL, finally we used the cleaned and stored data to build the dashboard
         using Tableau and deployed the dashboard using streamlit.
'''

st.markdown(howWeDidIT, unsafe_allow_html=True)

# canva pic that shows the process
processImage = Image.open('projectProcess.png')
st.image(processImage, width=480)

# links and socials
sociallinks = '''
    <p> Follow us! 
        <a href="https://github.com/DataPiece0">GitHub</a> |
        <a href="https://www.linkedin.com/in/zaid-allwansah-a09412227/">Zaid Hani</a> |
        <a href="https://www.linkedin.com/in/mohammad-aljermy-139b6b24a/">Mohammad Aljermy</a> |
        <a href="https://www.linkedin.com/in/ahmad-al-sheikh-ahmed-6b3a921a2/">Ahmad Ali</a> |
        <a href="https://www.linkedin.com/in/mahmood-abusaa-311389263/">Mahmoud Abusaa</a>

    </p>
'''
st.markdown(sociallinks, unsafe_allow_html=True)