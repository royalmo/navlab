#!/bin/bash

for lang_dir in app/translations/*; do
    if [ -d "$lang_dir" ]; then
        lang=$(basename "$lang_dir")
        #msgcat -o "$lang_dir/LC_MESSAGES/messages.po" "$lang_dir/LC_MESSAGES/**/*.po"
        # Can't use ** . Workaround:
        find "$lang_dir" -name '*.po' -print0 | xargs -0 msgcat -o "$lang_dir/LC_MESSAGES/messages.po"
    fi
done

pybabel compile -f -d app/translations
rm -f app/translations/*/LC_MESSAGES/messages.po
