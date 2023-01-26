
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogs_posted_date_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 17, 14, 55, 33, 719197)),
        ),
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
        
        migrations.RenameModel('Blogs', 'Blog')
    ]
    atomic = False
    
