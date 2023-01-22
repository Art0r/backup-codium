from prompt_toolkit.styles import Style

style_ok = Style.from_dict({
    'msg': '#50FC00 bold',
    'sub-msg': '#C3FFA7 italic'
})

style_fail = Style.from_dict({
    'msg': '#FF0000 bold',
    'sub-msg': '#FE8787 italic'
})
