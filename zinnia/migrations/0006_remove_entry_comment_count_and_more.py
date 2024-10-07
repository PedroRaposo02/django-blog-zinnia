import ctp_common.storages
from django.db import migrations, models
import zinnia.models_bases.entry


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0005_category_mptt_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='comment_enabled',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='pingback_count',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='pingback_enabled',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='trackback_count',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='trackback_enabled',
        ),
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, help_text='Used for illustration.', storage=ctp_common.storages.get_blog_media_storage, upload_to=zinnia.models_bases.entry.image_upload_to_dispatcher, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='related',
            field=models.ManyToManyField(blank=True, to='zinnia.entry', verbose_name='related entries'),
        ),
    ]
