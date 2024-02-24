from datetime import datetime

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import gettext_lazy as _

current_year = datetime.now().year
Year_Choices = tuple(zip(range(current_year - 100, current_year + 1), range(current_year - 100, current_year + 1)))[
               ::-1]

Month_CHOICES = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)


class Experience(models.Model):
    title = models.CharField(_('Title'), max_length=50, blank=False)
    company_name = models.CharField(_('Company Name'), max_length=50, blank=True, null=True)
    city = models.CharField(_('City'), max_length=10, blank=True, null=True)
    country = models.CharField(_('Province or country'), max_length=10, blank=True, null=True)
    start_year = models.IntegerField(_('Start Year'), choices=Year_Choices, blank=True, null=True)
    start_month = models.CharField(_('Start Month'), choices=Month_CHOICES, blank=True, null=True, max_length=10)
    end_year = models.IntegerField(_('End Year'), choices=Year_Choices, blank=True, null=True)
    end_month = models.CharField(_('End Month'), choices=Month_CHOICES, blank=True, null=True, max_length=10)
    is_present = models.BooleanField(_('I am currently working in this role'), default=False)
    industry = models.CharField(_('Industry'), max_length=50, blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)

    # relation
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Education(models.Model):
    school = models.CharField(_('School'), max_length=50, blank=False)
    degree = models.CharField(_('Degree'), max_length=50, blank=True, null=True)
    field_of_study = models.CharField(_('Field of Study'), max_length=200, blank=True, null=True)
    city = models.CharField(_('City'), max_length=10, blank=True, null=True)
    country = models.CharField(_('Province or country'), max_length=10, blank=True, null=True)
    start_year = models.IntegerField(_('Start Year'), choices=Year_Choices, blank=True, null=True)
    start_month = models.CharField(_('Start Month'), choices=Month_CHOICES, blank=True, null=True, max_length=10)
    end_year = models.IntegerField(_('End Year'), choices=Year_Choices, blank=True, null=True)
    end_month = models.CharField(_('End Month'), choices=Month_CHOICES, blank=True, null=True, max_length=10)
    grade = models.FloatField(_('Grade'))
    description = models.TextField(_('Description'), blank=True, null=True)
    # relation
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.school


class Certificate(models.Model):
    name = models.CharField(_('Name'), max_length=50, blank=False)
    issuing_organization = models.CharField(_('Issuing Organization'), max_length=50, blank=False)
    issue_year = models.IntegerField(_('Issue Year'), choices=Year_Choices, blank=True, null=True)
    issue_month = models.CharField(_('Issue Month'), choices=Month_CHOICES, blank=True, null=True, max_length=10)
    expiration_year = models.IntegerField(_('Expiration Year'), choices=Year_Choices, blank=True, null=True)
    expiration_month = models.CharField(_('Expiration Month'), choices=Month_CHOICES, blank=True, null=True,
                                        max_length=10)
    Credential_id = models.CharField(_('Credential Id'), max_length=20, blank=True, null=True)
    credential_url = models.URLField(_('Credential URL'))
    # relation
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Skill(models.Model):
    title_choices = (('git', 'git'), ('git_compare', 'git_compare'), ('git_branch', 'git_branch'),
                     ('git_commit', 'git_commit'), ('git_pull_request', 'git_pull_request'), ('git_merge', 'git_merge'),
                     ('bitbucket', 'bitbucket'), ('github_alt', 'github_alt'), ('github_badge', 'github_badge'),
                     ('github', 'github'), ('github_full', 'github_full'), ('java', 'java'), ('ruby', 'ruby'),
                     ('scala', 'scala'), ('python', 'python'), ('go', 'go'), ('ruby_on_rails', 'ruby_on_rails'),
                     ('django', 'django'), ('markdown', 'markdown'), ('php', 'php'), ('mysql', 'mysql'),
                     ('streamline', 'streamline'), ('database', 'database'), ('laravel', 'laravel'),
                     ('javascript', 'javascript'), ('angular', 'angular'), ('backbone', 'backbone'),
                     ('coffeescript', 'coffeescript'), ('jquery', 'jquery'), ('modernizr', 'modernizr'),
                     ('jquery_ui', 'jquery_ui'), ('ember', 'ember'), ('dojo', 'dojo'), ('nodejs', 'nodejs'),
                     ('nodejs_small', 'nodejs_small'), ('javascript_shield', 'javascript_shield'),
                     ('bootstrap', 'bootstrap'), ('sass', 'sass'), ('css3_full', 'css3_full'), ('css3', 'css3'),
                     ('html5', 'html5'), ('html5_multimedia', 'html5_multimedia'),
                     ('html5_device_access', 'html5_device_access'), ('html5_3d_effects', 'html5_3d_effects'),
                     ('html5_connectivity', 'html5_connectivity'), ('ghost_small', 'ghost_small'), ('ghost', 'ghost'),
                     ('magento', 'magento'), ('joomla', 'joomla'), ('jekyll_small', 'jekyll_small'),
                     ('drupal', 'drupal'), ('wordpress', 'wordpress'), ('grunt', 'grunt'), ('bower', 'bower'),
                     ('npm', 'npm'), ('yahoo_small', 'yahoo_small'), ('yahoo', 'yahoo'), ('bing_small', 'bing_small'),
                     ('windows', 'windows'), ('linux', 'linux'), ('ubuntu', 'ubuntu'), ('android', 'android'),
                     ('apple', 'apple'), ('appstore', 'appstore'), ('phonegap', 'phonegap'),
                     ('blackberry', 'blackberry'), ('stackoverflow', 'stackoverflow'), ('techcrunch', 'techcrunch'),
                     ('codrops', 'codrops'), ('css_tricks', 'css_tricks'), ('smashing_magazine', 'smashing_magazine'),
                     ('netmagazine', 'netmagazine'), ('codepen', 'codepen'), ('cssdeck', 'cssdeck'),
                     ('hackernews', 'hackernews'), ('dropbox', 'dropbox'), ('google_drive', 'google_drive'),
                     ('visualstudio', 'visualstudio'), ('unity_small', 'unity_small'), ('raspberry_pi', 'raspberry_pi'),
                     ('chrome', 'chrome'), ('ie', 'ie'), ('firefox', 'firefox'), ('opera', 'opera'),
                     ('safari', 'safari'), ('swift', 'swift'), ('symfony', 'symfony'),
                     ('symfony_badge', 'symfony_badge'), ('less', 'less'), ('stylus', 'stylus'), ('trello', 'trello'),
                     ('atlassian', 'atlassian'), ('jira', 'jira'), ('envato', 'envato'), ('snap_svg', 'snap_svg'),
                     ('raphael', 'raphael'), ('google_analytics', 'google_analytics'), ('compass', 'compass'),
                     ('onedrive', 'onedrive'), ('gulp', 'gulp'), ('atom', 'atom'), ('cisco', 'cisco'),
                     ('nancy', 'nancy'), ('clojure', 'clojure'), ('clojure_alt', 'clojure_alt'), ('perl', 'perl'),
                     ('celluloid', 'celluloid'), ('w3c', 'w3c'), ('redis', 'redis'), ('postgresql', 'postgresql'),
                     ('webplatform', 'webplatform'), ('jenkins', 'jenkins'), ('requirejs', 'requirejs'),
                     ('opensource', 'opensource'), ('typo3', 'typo3'), ('uikit', 'uikit'), ('doctrine', 'doctrine'),
                     ('groovy', 'groovy'), ('nginx', 'nginx'), ('haskell', 'haskell'), ('zend', 'zend'), ('gnu', 'gnu'),
                     ('yeoman', 'yeoman'), ('heroku', 'heroku'), ('debian', 'debian'), ('travis', 'travis'),
                     ('dotnet', 'dotnet'), ('codeigniter', 'codeigniter'), ('javascript_badge', 'javascript_badge'),
                     ('yii', 'yii'), ('msql_server', 'msql_server'), ('composer', 'composer'),
                     ('krakenjs_badge', 'krakenjs_badge'), ('krakenjs', 'krakenjs'), ('mozilla', 'mozilla'),
                     ('firebase', 'firebase'), ('sizzlejs', 'sizzlejs'), ('creativecommons', 'creativecommons'),
                     ('creativecommons_badge', 'creativecommons_badge'), ('mitlicence', 'mitlicence'),
                     ('senchatouch', 'senchatouch'), ('bugsense', 'bugsense'), ('extjs', 'extjs'),
                     ('mootools_badge', 'mootools_badge'), ('mootools', 'mootools'), ('ruby_rough', 'ruby_rough'),
                     ('komodo', 'komodo'), ('coda', 'coda'), ('bintray', 'bintray'), ('terminal', 'terminal'),
                     ('code', 'code'), ('responsive', 'responsive'), ('dart', 'dart'), ('aptana', 'aptana'),
                     ('mailchimp', 'mailchimp'), ('netbeans', 'netbeans'), ('dreamweaver', 'dreamweaver'),
                     ('brackets', 'brackets'), ('eclipse', 'eclipse'), ('cloud9', 'cloud9'), ('scrum', 'scrum'),
                     ('prolog', 'prolog'), ('terminal_badge', 'terminal_badge'), ('code_badge', 'code_badge'),
                     ('mongodb', 'mongodb'), ('meteor', 'meteor'), ('meteorfull', 'meteorfull'), ('fsharp', 'fsharp'),
                     ('rust', 'rust'), ('ionic', 'ionic'), ('sublime', 'sublime'), ('appcelerator', 'appcelerator'),
                     ('asterisk', 'asterisk'), ('aws', 'aws'), ('digital-ocean', 'digital-ocean'), ('dlang', 'dlang'),
                     ('docker', 'docker'), ('erlang', 'erlang'), ('google-cloud-platform', 'google-cloud-platform'),
                     ('grails', 'grails'), ('illustrator', 'illustrator'), ('intellij', 'intellij'),
                     ('materializecss', 'materializecss'), ('openshift', 'openshift'), ('photoshop', 'photoshop'),
                     ('rackspace', 'rackspace'), ('react', 'react'), ('redhat', 'redhat'), ('scriptcs', 'scriptcs'),
                     ('sqllite', 'sqllite'), ('vim', 'vim'))
    title = models.CharField(_('Title'), max_length=21, choices=title_choices)
    # relation
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    birth_date = models.DateField(_('Birth date'), blank=True, null=True, default=datetime.today)
    phone_number = models.CharField(_('Phone number'), max_length=20, blank=True, null=True)
    country = models.CharField(_('Province or country'), max_length=10, blank=True, null=True)
    city = models.CharField(_('City'), max_length=10, blank=True, null=True)
    postal_code = models.CharField(_('Postal code'), max_length=10, blank=True, null=True)
    street_address = models.CharField(_('Street address'), blank=True, null=True, max_length=50)
    professional_summary = models.TextField(_('Professional Summary'), blank=True, null=True)
    linkedin = models.URLField(_('LinkedIn'), blank=True, null=True)
    github = models.URLField(_('GitHub'), blank=True, null=True)
    twitter = models.URLField(_('Twitter'), blank=True, null=True)
    facebook = models.URLField(_('Facebook'), blank=True, null=True)
    interests = models.TextField(_('Interests'), blank=True, null=True)
    hide_sensitive = models.BooleanField(_('Hide Sensitive'), default=False)
    resume = models.FileField('Resume', upload_to='resume/')
    # Relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_birth_date(self):
        if self.birth_date is not None:
            month = "{}".format(self.birth_date.month).zfill(2)
            day = "{}".format(self.birth_date.day).zfill(2)
            year = "{}".format(self.birth_date.year)
        else:
            month = '01'
            day = '01'
            year = '0001'

        return '{}-{}-{}'.format(year, month, day)

    def __str__(self):
        return self.user.username
