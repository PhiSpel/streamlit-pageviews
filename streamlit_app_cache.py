import streamlit as st

@st.cache(allow_output_mutation=True)
def global_page_views(gpv = 0):
    gpv += 1 # this will only be run once because after the first execution the cache will be referenced
    return gpv
    
@st.cache(allow_output_mutation=True)
def session_execution_counter(sec = 0):
    sec += 1 # this will only be run once because after the first execution the cache will be referenced
    return sec

@st.cache(allow_output_mutation=True)
def session_execution_counter_history(sec_history = []):
    sec_history.append(sec_history) # this will only be run once because after the first execution the cache will be referenced
    return sec_history

st.title('Trying out page view counts with caching.')
    
if not 'session_executions' in st.session_state:
    # this will only be run once per session
    gpv = global_page_views() # initialize the global page views variable (activates the cache)
    gpv = global_page_views(gpv) # updating gpv by 1
    #page_views = page_view_counter(page_views)
    sec = session_execution_counter() # get the sec from previous session
    sec_history = session_execution_counter_history() # get sec history from global cache
else:
    sec = session_execution_counter() # getting sec from global cache
    gpv = global_page_views()
    sec_history = session_execution_counter_history()
    
    
st.write('current page views: ' + str(gpv))
st.write('current session executions: ' + str(sec))
st.write('previous session executions: ' + str(sec_history))

st.button('rerun')
