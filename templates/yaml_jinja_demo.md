

```python
interface_name = 'ge-0/0/1'
print interface_name
```

    ge-0/0/1



### Python List


```python
protocols = ['mpls', 'bgp', 'isis', 'ospf']
```


```python
for prot in protocols:
    print prot
```

    mpls
    bgp
    isis
    ospf


### Python Dictionary


```python
data = {'company': 'Juniper',
       'ceo': 'Rami Rahim',
       'domain': 'Networking'}

print data
```

    {'ceo': 'Rami Rahim', 'company': 'Juniper', 'domain': 'Networking'}



```python
for k,v in data.items():
    print k, ' -> ', v
```

    ceo  ->  Rami Rahim
    company  ->  Juniper
    domain  ->  Networking



```python
data = {'iface_name':'ge-0/0/1', 'vlan_name':'200'}
print data
```

    {'vlan_name': '200', 'iface_name': 'ge-0/0/1'}


# YAML

### YAML is a human friendly data serialization standard for all programming languages. It is ideal for storing object tree.

### Python programmers are generally big fans of YAML, because of the use of indentation, rather than bracketed syntax, to indicate levels.

### A markup language is a language that annotates text so that the computer can manipulate the text.


```yaml
---
# An employee record
name: Example Developer 
job: Developer 
skill: Elite 
employed: True 
foods:     
    - Apple     
    - Orange     
    - Strawberry     
    - Mango 
languages:     
    ruby: Elite     
    python: Elite     
    dotnet: Lame
```

#### Thumb rule to write YAML: Proper indentation. 

So what are the benefits of YAML:

Portable between programming languages:

YAML emitters and parsers for many popular languages written in the pure native language itself exist, making it portable in a self-contained manner. 
YAML representations of application information will be consistent and portable between various programming environments

Well known libraries to play with YAML in programming language:
C/C++:   
- libyaml       	# "C" Fast YAML 1.1 
Ruby:   
- Psych         	# libyaml wrapper (in Ruby core for 1.9.2)   
- RbYaml        	# YAML 1.1 (PyYaml Port) binding   
Python:   
- PyYaml        	# YAML 1.1, pure python and libyaml binding   
- PySyck        	# YAML 1.0, syck binding   
Java:   
- JvYaml        	# Java port of RbYaml   
Perl Modules:   
- YAML          	# Pure Perl YAML Module   
- YAML::Syck    	# Binding to libsyck   
- PlYaml        	# Perl port of PyYaml implementation
PHP:   
- php-yaml      	# libyaml bindings (YAML 1.1)   
- syck          	# syck bindings (YAML 1.0)   


### Another example

```yaml
---
name: Juniper Networks 
CEO: Rami Rahim
Headquarter: Sunnyvale
Development:     
    - Sunnyvale
    - Bangalore
    - Beijing
Sales:     
    - Sydeny
    - Mumbai
```


```python
import yaml

data = """
---
name: Juniper Networks 
CEO: Rami Rahim
Headquarter: Sunnyvale
Development:     
    - Sunnyvale
    - Bangalore
    - Beijing
Sales:     
    - Sydeny
    - Mumbai
"""

yaml.load(data)
```




    {'CEO': 'Rami Rahim',
     'Development': ['Sunnyvale', 'Bangalore', 'Beijing'],
     'Headquarter': 'Sunnyvale',
     'Sales': ['Sydeny', 'Mumbai'],
     'name': 'Juniper Networks'}




```python
data = """
---
-
    - pineapple   
    - coconut 
-
    - umbrella   
    - raincoat
"""
yaml.load(data)
```




    [['pineapple', 'coconut'], ['umbrella', 'raincoat']]




```python
data = """
---
Joey:   
    age: 22   
    sex: M 
Laura:   
    age: 24   
    sex: F
"""
yaml.load(data)
```




    {'Joey': {'age': 22, 'sex': 'M'}, 'Laura': {'age': 24, 'sex': 'F'}}




```python
data = """
---
receipt:     Oz-Ware Purchase Invoice
date:        2012-08-06
customer:
    first_name:   Dorothy
    family_name:  Gale

items:
    - part_no:   A4786
      descrip:   Water Bucket (Filled)
      price:     1.47
      quantity:  4

    - part_no:   E1628
      descrip:   High Heeled "Ruby" Slippers
      size:      8
      price:     133.7
      quantity:  1

bill-to:  &id001
    street: |
            123 Tornado Alley
            Suite 16
    city:   East Centerville
    state:  KS

ship-to:  *id001

specialDelivery:  >
    Follow the Yellow Brick
    Road to the Emerald City.
    Pay no attention to the
    man behind the curtain.
...
"""
yaml.load(data)
```




    {'bill-to': {'city': 'East Centerville',
      'state': 'KS',
      'street': '123 Tornado Alley\nSuite 16\n'},
     'customer': {'family_name': 'Gale', 'first_name': 'Dorothy'},
     'date': datetime.date(2012, 8, 6),
     'items': [{'descrip': 'Water Bucket (Filled)',
       'part_no': 'A4786',
       'price': 1.47,
       'quantity': 4},
      {'descrip': 'High Heeled "Ruby" Slippers',
       'part_no': 'E1628',
       'price': 133.7,
       'quantity': 1,
       'size': 8}],
     'receipt': 'Oz-Ware Purchase Invoice',
     'ship-to': {'city': 'East Centerville',
      'state': 'KS',
      'street': '123 Tornado Alley\nSuite 16\n'},
     'specialDelivery': 'Follow the Yellow Brick\nRoad to the Emerald City.\nPay no attention to the\nman behind the curtain.\n'}




```python
data = """
---
- step:  &id001                  # defines anchor label &id001
    instrument:      Lasik 2000
    pulseEnergy:     5.4
    pulseDuration:   12
    repetition:      1000
    spotSize:        1mm

- step: &id002
    instrument:      Lasik 2000
    pulseEnergy:     5.0
    pulseDuration:   10
    repetition:      500
    spotSize:        2mm
- step: *id001                   # refers to the first step (with anchor &id001)
- step: *id002                   # refers to the second step
- step: 
    <<: *id001
    spotSize: 2mm             # redefines just this key, refers rest from &id001
"""
yaml.load(data)
```




    [{'step': {'instrument': 'Lasik 2000',
       'pulseDuration': 12,
       'pulseEnergy': 5.4,
       'repetition': 1000,
       'spotSize': '1mm'}},
     {'step': {'instrument': 'Lasik 2000',
       'pulseDuration': 10,
       'pulseEnergy': 5.0,
       'repetition': 500,
       'spotSize': '2mm'}},
     {'step': {'instrument': 'Lasik 2000',
       'pulseDuration': 12,
       'pulseEnergy': 5.4,
       'repetition': 1000,
       'spotSize': '1mm'}},
     {'step': {'instrument': 'Lasik 2000',
       'pulseDuration': 10,
       'pulseEnergy': 5.0,
       'repetition': 500,
       'spotSize': '2mm'}},
     {'step': {'instrument': 'Lasik 2000',
       'pulseDuration': 12,
       'pulseEnergy': 5.4,
       'repetition': 1000,
       'spotSize': '2mm'}}]




```python
yaml.parse?
```

## Jinja2

### Junos sample config


```python
import os
cwd = os.getcwd()
print cwd
```

    /Users/nitinkr/Coding/pyez-examples/templates



```python
from jinja2 import Template
t = Template("Hello {{ data }}!!")
print t.render(data='xyz')
```

    Hello xyz!!


```text
interfaces {
    interface ge-0/0/1 {
        unit 0 {
            family ethernet-switching {
                port-mode access;
                replace:
                vlan {
                    member 200;
               }
           }
       }
    } 
}
```


### jinja2 template

```jinja2
interfaces {
    interface {{ iface_name }} {
        unit 0 {
            family ethernet-switching {
                port-mode access;
                replace:
                vlan {
                    member {{ vlan_name }};
               }
           }
       }
    } 
}
```



```python
import jinja2
template = """interfaces {
    interface {{ iface_name }} {
        unit 0 {
            family ethernet-switching {
                port-mode access;
                replace:
                vlan {
                    member {{ vlan_name }};
               }
           }
       }
    } 
}"""
tmpl = jinja2.Template(template)
conf = tmpl.render(iface_name='ge-0/0/2', vlan_name='200')
print conf
```

    interfaces {
        interface ge-0/0/2 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 200;
                   }
               }
           }
        } 
    }



```python
import jinja2
template = """interfaces {
    interface {{ iface_name }} {
        unit 0 {
            family ethernet-switching {
                port-mode access;
                replace:
                vlan {
                    member {{ vlan_name }};
               }
           }
       }
    } 
}"""
tmpl = jinja2.Template(template)
conf = tmpl.render({'iface_name':'ge-0/0/1', 'vlan_name':'200'})
print conf
```

    interfaces {
        interface ge-0/0/1 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 200;
                   }
               }
           }
        } 
    }



```python
import jinja2

# tmpl = jinja2.Template(open('/Users/nitinkr/demos/PyEZ/templates/1_temp.j2').read())

loader = jinja2.FileSystemLoader(cwd)
jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
tmpl = jenv.get_template('1_temp.j2')
conf = tmpl.render(iface_name='ge-0/0/5', vlan_name='300')
print conf
```

    interfaces {
        interface ge-0/0/5 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           }
        } 
    }


#### To know more about trim_blocks, lstrip_blocks

http://jinja.pocoo.org/docs/dev/templates/#whitespace-control


```python
jinja2.Environment?
```

### Loop inside Jinja Template

```jinja2
interfaces {
    {% for item in interfaces %}
    {{ item }} {
        unit 0 {
            family ethernet-switching {
                port-mode access;
                replace:
                vlan {
                    member {{ vlan_name }};
               }
           }
       } 
    } {% endfor %}    
}
```


```python
import jinja2
template = """interfaces {
    {% for item in interfaces %}
    {{ item }} {
        unit 0 {
            family ethernet-switching {
                port-mode access;
                replace:
                vlan {
                    member {{ vlan_name }};
               }
           }
       } 
    } {% endfor %}    
}"""
tmpl = jinja2.Template(template)
conf = tmpl.render(interfaces=['ge-0/0/1', 'ge-0/0/2', 'ge-0/2/1', 'ge-0/2/2'], vlan_name='300')
print conf
```

    interfaces {
        
        ge-0/0/1 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        } 
        ge-0/0/2 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        } 
        ge-0/2/1 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        } 
        ge-0/2/2 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     
    }


### Filter in Template


```python
loader = jinja2.FileSystemLoader(cwd)
jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
```


```python
import jinja2
template = """interfaces {
    {% for item in interfaces %}
    {{ item }} {
        unit 0 {
            family ethernet-switching {
                port-mode {{ mode | upper }};
                replace:
                vlan {
                    member {{ vlan_name }};
               }
           }
       } 
    } {% endfor %}    
}"""
tmpl = jinja2.Template(template)
conf = tmpl.render(interfaces=['ge-0/0/1', 'ge-0/0/2'], vlan_name='300', mode='access')
print conf
```

    interfaces {
        
        ge-0/0/1 {
            unit 0 {
                family ethernet-switching {
                    port-mode ACCESS;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        } 
        ge-0/0/2 {
            unit 0 {
                family ethernet-switching {
                    port-mode ACCESS;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     
    }



```python
jenv.filters
```


```python
from bracket_expansion import bracket_expansion
jenv.filters['bracket_expansion']=bracket_expansion
for i in bracket_expansion('ge-0/0/[0-5]'):
    print i
```

    ge-0/0/0
    ge-0/0/1
    ge-0/0/2
    ge-0/0/3
    ge-0/0/4
    ge-0/0/5



```python
import jinja2
template = """interfaces {
    {% for item in iface_pattern | bracket_expansion %}
    {{ item }} {
        unit 0 {
            family ethernet-switching {
                port-mode access;
                replace:
                vlan {
                    member {{ vlan_name }};
               }
           }
       } 
    } {% endfor %}    
}"""
loader = jinja2.FileSystemLoader(cwd)
jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
jenv.filters['bracket_expansion']=bracket_expansion
tmpl = jenv.get_template('filter.j2')
conf = tmpl.render(iface_pattern='ge-0/0/[0-10]', vlan_name='300')
print conf
```

    interfaces {
        ge-0/0/0 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     ge-0/0/1 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     ge-0/0/2 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     ge-0/0/3 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     ge-0/0/4 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     ge-0/0/5 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     ge-0/0/6 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     ge-0/0/7 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     ge-0/0/8 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     ge-0/0/9 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     ge-0/0/10 {
            unit 0 {
                family ethernet-switching {
                    port-mode access;
                    replace:
                    vlan {
                        member 300;
                   }
               }
           } 
        }     
    }


### Include directive
#### To create Modular template


```python
from glob import glob
print glob(cwd+'/sshkeys/*.pub')
```

    ['/Users/nitinkr/Coding/pyez-examples/templates/sshkeys/lakhan.pub', '/Users/nitinkr/Coding/pyez-examples/templates/sshkeys/ram.pub']



```python
from os.path import basename, splitext
print [basename(i) for i in glob(cwd+'/sshkeys/*.pub')]
print [splitext(basename(i))[0] for i in glob(cwd+'/sshkeys/*.pub')]
```

    ['lakhan.pub', 'ram.pub']
    ['lakhan', 'ram']



```python
def basefilename(name):
    return splitext(basename(name))[0]

# basefilename = lambda name: splitext(basename(name))[0]
```

```jinja2
system {
    login {
        {% for ssh_pub in sshkeyfiles %}
        user {{ ssh_pub | basefilename }} {
            authentication {
                ssh-rsa "{% include ssh_pub %}";
            }
        }
        {% endfor %}
    }
}
```


```python
import jinja2

loader = jinja2.FileSystemLoader(cwd)
jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
jenv.filters['basefilename']=basefilename
tmpl = jenv.get_template('users.j2')
print tmpl.render(sshkeyfiles=glob('sshkeys/*.pub'))
```

    system {
        login {
            user lakhan {
                authentication {
                    ssh-rsa "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCl2uGO4skBv30W3O6//E2h4wmagnp5F2d2ZAejG+rozy+fbAD83nD4cOg5PZfpVTmV5q3VitcG7rQlRim4Rw+669R+n06BG/FarsIv2yAV9Vz30y51tlzCThF4TQEVttKgQtdmgtenoTOnIsZHjms6zx7OyeMws4nb6kFE1eFv2A+h+FAQeIq+5bxXWpH77Wr9DrCVS6wqyDu4niv6WnxshJFKO8AZOkl51qcQznEe9J7Jz4SfgXnqGKJsJnJOGSdxK6gyRRLYLQ2S7CZIQe6Cb97nGERFSx4w9XFMWZf/RkY3o0lXOv0VC51pr5ocJYvb+IpYAiCjF0po6xMd11dh nitinkr@nitinkr-mba13";
                }
            }
            user ram {
                authentication {
                    ssh-rsa "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDDHSljc8AuY2UgmZuAl5hW18UZJwzj4u1Qu6kWJ4aecK71r3Vrar65TKNisv/eOOFVHoI8690IOMHG0NUzNJH+WtaFFKhI/2yX6Q3UJ8Chs3FOIfRvMtORvgrN5JJfKREmRVEWVdzWqHDGs6DyXDiL8h0XsBQmCJcuMS5JCi+GggYr/ysMOzLXWkjgZasj0AcVZrGkaTV0R1Ec7SV/IZGMZC1RelDiaTiMPdsI7LFV6jnZzqG9IZmMHwDLAocO/HN2nnGUWGBn172h8ah0fSuTnA8Wm5AnD+/3k/N5tHOjMfRU+P755FWkC+TwPuXrtqV8kh4ZBWWr5CHUtflzNmMn nitinkr@nitinkr-mba13";
                }
            }
        }
    }



```python
with open(os.path.join(cwd, 'main.j2')) as fp:
    print fp.read()
```

    ##
    ## This is top main file
    ##
    
    interfaces { 
        {% for item in interfaces %}
        {{ item }} {
            description "{{ description }}";
            unit 0 {
                family {{ family }};
            }      
        } {% endfor %}    
    }
    ##
    ## including another jinja templete
    ##
    {% include 'users.j2' %}
    
    ##
    ## thats the end
    ##
    



```python
main = jenv.get_template('main.j2')
print main.render(sshkeyfiles=glob('sshkeys/*.pub'), interfaces=['ge-0/0/1', 'ge-0/0/2'], family='mpls', description='MPLS interface')
```

    ##
    ## This is top main file
    ##
    
    interfaces { 
        ge-0/0/1 {
            description "MPLS interface";
            unit 0 {
                family mpls;
            }      
        }     ge-0/0/2 {
            description "MPLS interface";
            unit 0 {
                family mpls;
            }      
        }     
    }
    ##
    ## including another jinja templete
    ##
    system {
        login {
            user lakhan {
                authentication {
                    ssh-rsa "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCl2uGO4skBv30W3O6//E2h4wmagnp5F2d2ZAejG+rozy+fbAD83nD4cOg5PZfpVTmV5q3VitcG7rQlRim4Rw+669R+n06BG/FarsIv2yAV9Vz30y51tlzCThF4TQEVttKgQtdmgtenoTOnIsZHjms6zx7OyeMws4nb6kFE1eFv2A+h+FAQeIq+5bxXWpH77Wr9DrCVS6wqyDu4niv6WnxshJFKO8AZOkl51qcQznEe9J7Jz4SfgXnqGKJsJnJOGSdxK6gyRRLYLQ2S7CZIQe6Cb97nGERFSx4w9XFMWZf/RkY3o0lXOv0VC51pr5ocJYvb+IpYAiCjF0po6xMd11dh nitinkr@nitinkr-mba13";
                }
            }
            user ram {
                authentication {
                    ssh-rsa "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDDHSljc8AuY2UgmZuAl5hW18UZJwzj4u1Qu6kWJ4aecK71r3Vrar65TKNisv/eOOFVHoI8690IOMHG0NUzNJH+WtaFFKhI/2yX6Q3UJ8Chs3FOIfRvMtORvgrN5JJfKREmRVEWVdzWqHDGs6DyXDiL8h0XsBQmCJcuMS5JCi+GggYr/ysMOzLXWkjgZasj0AcVZrGkaTV0R1Ec7SV/IZGMZC1RelDiaTiMPdsI7LFV6jnZzqG9IZmMHwDLAocO/HN2nnGUWGBn172h8ah0fSuTnA8Wm5AnD+/3k/N5tHOjMfRU+P755FWkC+TwPuXrtqV8kh4ZBWWr5CHUtflzNmMn nitinkr@nitinkr-mba13";
                }
            }
        }
    }
    ##
    ## thats the end
    ##


### if/then/else directives


```python
import csv
vlans = csv.DictReader(open(os.path.join(cwd,'vlans.csv')))
print vlans
for i in vlans:
    print i,','
```

    <csv.DictReader instance at 0x104af7170>
    {'vlan_id': '100', 'vlan_name': 'Blue'} ,
    {'vlan_id': '200', 'vlan_name': 'Green'} ,
    {'vlan_id': '300', 'vlan_name': 'Yellow'} ,
    {'vlan_id': '400', 'vlan_name': 'Purple'} ,
    {'vlan_id': '500', 'vlan_name': 'Red'} ,



```python
import jinja2

vlans = csv.DictReader(open(os.path.join(cwd,'vlans.csv')))
loader = jinja2.FileSystemLoader(cwd)
jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
tmpl = jenv.get_template('main_vlans.conf')
print tmpl.render(vlan_list=vlans)
```

    
    vlans {
        Blue {
            vlan-id 100;
        }
        Green {
            vlan-id 200;
        }
        Yellow {
            vlan-id 300;
        }
        Purple {
            vlan-id 400;
        }
        Red {
            vlan-id 500;
        }
    }



```python
vlans = csv.DictReader(open(os.path.join(cwd,'vlans.csv')))
print tmpl.render(vlan_list=vlans, state='absent')
```

    
    vlans {
        delete: Blue
        delete: Green
        delete: Yellow
        delete: Purple
        delete: Red
    }


### This presentation from AnsibleFest San Francisco 2015 focused on how Riot Games utilizes Ansible, Config templates  and Juniper’s Py-EZ.


```python
from IPython.display import HTML
HTML('<iframe src="http://fast.wistia.net/embed/iframe/qkho0rgeyc" width=900 height=500></iframe>')
```




<iframe src="http://fast.wistia.net/embed/iframe/qkho0rgeyc" width=900 height=500></iframe>




```python
from IPython.display import YouTubeVideo
YouTubeVideo('PSgSjTeqRX0', start=450, width=900, height=500)
```





        <iframe
            width="900"
            height="500"
            src="https://www.youtube.com/embed/PSgSjTeqRX0?start=450"
            frameborder="0"
            allowfullscreen
        ></iframe>
        




```python
from IPython.display import YouTubeVideo
YouTubeVideo('Gk5KKozJmz8', start=156, width=900, height=500)
```





        <iframe
            width="900"
            height="500"
            src="https://www.youtube.com/embed/Gk5KKozJmz8?start=156"
            frameborder="0"
            allowfullscreen
        ></iframe>
        


