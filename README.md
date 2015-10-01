Oracle Database 11R2
=====

Version 1.0-43p
-------------

![](http://www.oracle.com/ocom/groups/public/@otn/documents/digitalasset/123455.gif)

Installs and configures Oracle Database 11R2.
Currently only Enterprise Edition is supported.

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.tonomi.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-oracle-db/1.0-43p/meta.yml)

Features
--------

 - Install and configure Oracle Database 11R2
 - Create users/schemas
 - Manage grants
 - Execute arbitrary SQL

Pre-requisites
--------------

 - AWS account
 - Centos 6 x86_64 ([AWS Marketplace](https://aws.amazon.com/marketplace/pp/B00A6KUVBW))
 - Oracle Database installation files (version 11.2.0.4 is preferred) ([Download](http://www.oracle.com/technetwork/database/enterprise-edition/downloads/index.html))

Configuration
-------------

 - Launch/configure Cloud Account in desired region:
   - N.California (us-west-1)
   - Oregon (us-west-2)
   - N.Virginia (us-east-1)
 - Create enviroment property `oracle_db_ee_install` with type `map<string, object>` and contents:
```
disks:
  - "http://url.to/disk1of2"
  - "http://url.to/disk2of2"
```
