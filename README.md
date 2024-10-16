# append_shader_usage_example
This example program showcases how to use complexpbr's composition functionality by supplying body and main-loop modifications.

## Minimal Usage:
```python
# example excerpt
# call the append_shader() function
custom_body_mod = 'float default_noise(vec2 n)\n{\nfloat n2  = fract(sin(dot(n.xy,vec2(11.78,77.443)))*44372.7263);\nreturn n2;\n}'
custom_main_mod = 'o_color += default_noise(vec2(3.3));'
complexpbr.append_shader(test_sphere, custom_body_mod, custom_main_mod)
```
