import subprocess

def hdfs(node, dir):
    with open('/etc/hadoop/hdfs-site.xml', 'w') as fp:
        fp.write(f"""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n
<!-- Put site-specific property overrides in this file. -->\n
<configuration>
<property>
<name>dfs.{node}.dir</name>
<value>{dir}</value>
</property>
</configuration>\n""")

def core(ip, port):
    with open('/etc/hadoop/core-site.xml', 'w') as fp:
        fp.write(f"""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n
<!-- Put site-specific property overrides in this file. -->\n
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{ip}:{port}</value>
</property>
</configuration>\n""")

def start(node):
    if node == 'namenode':
        subprocess.run(['hadoop', 'namenode', '-format'], stdout=subprocess.DEVNULL)

    subprocess.run(['hadoop-daemon.sh', 'start', node], stdout=subprocess.DEVNULL)
