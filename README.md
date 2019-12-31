# conan-libcoap


[![Conan](https://api.bintray.com/packages/gocarlos/public-conan/libcoap:gocarlos/images/download.svg) ](https://bintray.com/gocarlos/public-conan/libcoap:gocarlos/_latestVersion)

## lib producer

```bash
# build conan package
conan create . gocarlos/testing --build missing
# upload package to gocarlos artifactory
conan upload libcoap -r gocarlos
```

## lib consumer

```bash
conan remote add gocarlos https://api.bintray.com/conan/gocarlos/public-conan

cat << EOF >> conanfiile.txt
[requires]
libcoap/4.3.0@gocarlos/testing

[generators]
cmake_find_package
cmake_paths

[options]
EOF
```
