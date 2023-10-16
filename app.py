import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(layout='wide',   page_icon='airbnblogo.png', page_title='New York')

st.write('please use light mode for a better view')

title='''
<h1 style="color:black">AirBNB in New York</h1>
'''
image = Image.open('airbnb.png')

st.markdown(title, unsafe_allow_html=True)
st.image(image, width=200)

description ='''
<p style="color:black">
    Welcome to our project! in this project we will showcase our skills that we have obtained as students,
    we have made this project by getting a dataset about the AirBNB company from kaggle, this dataset is only set in New York in the Uinted States.
    After we got the dataset we cleaned it using Python in Jupyter Notebook, after that we used Tableau as a visualization tool to make our
    dashboard interactive, and finally we used streamlit as a way to write some of the html and host our project.
</p>
'''

st.markdown(description, unsafe_allow_html=True)



jermey_code = """
<div class='tableauPlaceholder' id='viz1697475590448' style='position: relative'><noscript><a href='#'><img alt='Dashboard 7 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;te&#47;test1_16972309187040&#47;Dashboard7&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='test1_16972309187040&#47;Dashboard7' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;te&#47;test1_16972309187040&#47;Dashboard7&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1697475590448');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='2077px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

"""


#components.html(zaid_code, height=1000)
components.html(jermey_code, height=2100)

st.write(
'''

''')