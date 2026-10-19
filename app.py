"""
Web page for the linguistic anti-pattern tool.

Run it with:  streamlit run app.py
"""
import difflib
import os

import pandas as pd
import streamlit as st

from lap_engine import LAP_NAMES, FIX_ORDER, run

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, 'Demo-backup.txt')) as f:
    EXAMPLE_CODE = f.read()

st.set_page_config(page_title='Linguistic anti-patterns', page_icon='🔤', layout='wide')

st.title('Linguistic anti-patterns in Java')
st.caption('Finds methods whose name promises one thing while the code does another, '
           'and rewrites them so name and behaviour agree.')

check_tab, about_tab = st.tabs(['Check your code', 'What it looks for'])

# =====================================================================
# check your code
# =====================================================================
with check_tab:
    source = st.radio('Code to check', ['Example', 'Paste code', 'Upload a .java file'], horizontal=True)

    file_name = 'Demo.java'
    code = ''
    if source == 'Example':
        code = EXAMPLE_CODE
        with st.expander('Show the example code'):
            st.code(code, language='java')
    elif source == 'Paste code':
        code = st.text_area('Java code (one class)', height=300, placeholder='public class MyClass { ... }')
        file_name = 'Fixed.java'
    else:
        uploaded = st.file_uploader('Java file', type=['java'])
        if uploaded is not None:
            code = uploaded.getvalue().decode('utf-8', errors='replace')
            file_name = uploaded.name

    remove_empty = st.checkbox('Also remove empty methods', value=False,
                               help='A method with an empty body is a "not implemented" anti-pattern. '
                                    'Tick this to delete such methods too.')

    if st.button('Find and fix', type='primary', disabled=not code.strip()):
        st.session_state['result'] = run(code, remove_empty)
        st.session_state['original'] = code.replace('\r\n', '\n')
        st.session_state['file_name'] = file_name
        st.session_state['remove_empty'] = remove_empty

    # Kept in session_state so the results stay on screen after a download click.
    if 'result' in st.session_state:
        result = st.session_state['result']
        original = st.session_state['original']
        types = [t for t in FIX_ORDER if st.session_state['remove_empty'] or t != 5]

        st.divider()
        if result['error']:
            st.warning(result['error'])

        found = result['found']
        left, right = st.columns([1, 2])
        with left:
            st.metric('Anti-patterns found', len(found))
            counts = pd.DataFrame({
                'Anti-pattern': [LAP_NAMES[t] for t in types],
                'Count': [sum(1 for f in found if f[0] == t) for t in types],
            })
            st.dataframe(counts, hide_index=True, width="stretch")
        with right:
            if found:
                st.markdown('**Where they are**')
                table = pd.DataFrame(found, columns=['Type', 'Method', 'Line'])
                table['Type'] = table['Type'].map(LAP_NAMES)
                st.dataframe(table.rename(columns={'Type': 'Anti-pattern'}), hide_index=True,
                             width="stretch")
            else:
                st.success('No anti-patterns found. The method names match what the methods do.')

        if result['steps']:
            st.markdown('**What was changed**')
            st.markdown('\n'.join(f'{i}. {s}' for i, s in enumerate(result['steps'], 1)))

        fixed = result['fixed_code']
        if fixed != original:
            fixed_tab, diff_tab, original_tab = st.tabs(['Fixed code', 'Changes', 'Original code'])
            with fixed_tab:
                st.code(fixed, language='java', line_numbers=True)
            with diff_tab:
                diff = difflib.unified_diff(original.splitlines(), fixed.splitlines(),
                                            'original', 'fixed', lineterm='')
                st.code('\n'.join(diff), language='diff')
            with original_tab:
                st.code(original, language='java', line_numbers=True)
            st.download_button('Download the fixed file', fixed, file_name=st.session_state['file_name'],
                               mime='text/x-java-source')

# =====================================================================
# what it looks for
# =====================================================================
with about_tab:
    st.markdown('''
A **linguistic anti-pattern** is a mismatch between a method's name and what the
method really does. The reader trusts the name and is misled. The tool reads the
first word of each method name (`get`, `is`, `set`), checks the method body and
return type, and fixes the mismatch.

| Anti-pattern | What is wrong | How the tool fixes it |
|---|---|---|
| "Get" more than an accessor | `getX()` does real work (several statements, or an `if`) instead of just returning a value | moves the work into a new method `complement_getX()`; `getX()` only returns its result |
| Get method does not return | `getX()` returns `void` | renames it `calculateForgetX()` |
| Is returns more than a boolean | `isX()` returns a number, a text or an array | `isX()` now returns `boolean`; the old body moves to `complement_isX()` |
| Set method returns | `setX()` returns a value | it becomes `void` and is renamed `setX_WithLog()`; the value goes into a new field `logFor_setX` |
| Not implemented method | the body is empty | removes the method (only when you tick the box) |

**Limits**

- The parser (javalang) reads Java up to version 8. Newer syntax such as `var`,
  records or switch expressions gives an error.
- Give it one class per file: new methods are added before the last `}` of the file.
- Only names that start with exactly `get`, `is` or `set` are checked.
- Renaming is plain text replacement inside this one file. Calls from other files
  are not updated.
''')
