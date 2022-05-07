import streamlit as st

#@st.cache()
#def page_view_counter(page_views):
#    page_view_counter+=1
#    return page_view_counter
    
@st.cache()
def global_page_views():
    return global_page_views
    
@st.chache()
def session_execution_counter(session_executions):
    session_executions+=1
    return session_executions
    
if not 'some_variable' in st.session_state:
    gpv = global_page_views()
    gpv += 1
    #page_views = page_view_counter(page_views)
    st.session_state['some_variable'] = 'something'
    
session_executions = 0
session_execution_counter(session_executions)
    
st.write('current page views: ' + str(page_views))
st.write('current session executions: ' + str(session_executions))

st.button('rerun')
