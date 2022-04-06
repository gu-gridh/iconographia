# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

def get_fields(model: models.Model, exclude=['id']):
    return [field.name for field in model._meta.fields if field.name not in exclude]

class ColLabels(models.Model):
    tab = models.CharField(max_length=32)
    col = models.CharField(max_length=32)
    label = models.CharField(max_length=255, blank=True, null=True)
    label_sv = models.CharField(max_length=255, blank=True, null=True)
    ftab = models.CharField(max_length=32, blank=True, null=True)
    fcol = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    hidden = models.PositiveIntegerField()
    readonly = models.PositiveIntegerField()
    searchable = models.PositiveIntegerField()
    help = models.CharField(max_length=256)
    help_sv = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'col_labels'


class Image(models.Model):
    bild = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.image.image"))
    bildfil = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.image.image_file"))
    mb_object = models.ForeignKey('Object', models.DO_NOTHING, verbose_name=_("iconographia.image.object"))

    class Meta:
        managed = False
        db_table = 'image'
        verbose_name = _("iconographia.image.meta.singular_name")
        verbose_name_plural = _("iconographia.image.meta.plural_name")

    def __str__(self) -> str:
        return f"{self.mb_object} ({self.bildfil})"

class Motive(models.Model):
    mb_image = models.ForeignKey(Image, models.DO_NOTHING, verbose_name=_("iconographia.motive.image"))
    motive = models.CharField(max_length=175, blank=True, null=True, verbose_name=_("iconographia.motive.motif"))

    class Meta:
        managed = False
        db_table = 'motive'
        verbose_name = _("iconographia.motive.meta.singular_name")
        verbose_name_plural = _("iconographia.motive.meta.plural_name")

    def __str__(self) -> str:
        return f"{self.motive}: {self.mb_image}"

class Object(models.Model):
    objektid = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.object_id"))
    main_image = models.ForeignKey(Image, models.DO_NOTHING, db_column='main_image', verbose_name=_("iconographia.object.main_image"))
    museum = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.museum"))
    inventarienummer = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.inventory_nr"))
    undernummer = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.sub_nr"))
    invnr = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.inv_nr"))
    landskap = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.county"))
    ort = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.town"))
    sakord = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.topic"))
    typ = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.type"))
    undertyp = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.subtype"))
    cdh_category = models.CharField(max_length=16, verbose_name=_("iconographia.object.cdh_category"))
    objekt = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.object"))
    namntyp = models.PositiveIntegerField(blank=True, null=True, verbose_name=_("iconographia.object.name_type"))
    upphovsman = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.author"))
    tid = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.time"))
    lk_tid = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.time_lk"))
    dat_min = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_("iconographia.object.dat_min"))
    dat_max = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_("iconographia.object.dat_max"))
    hojd = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.height"))
    bredd = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.width"))
    material = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.material"))
    delar = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.parts"))
    urtappning = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.urtappning"))
    inskrift = models.CharField(max_length=256, blank=True, null=True, verbose_name=_("iconographia.object.inscription"))
    kondition = models.CharField(max_length=512, blank=True, null=True, verbose_name=_("iconographia.object.condition"))
    farg = models.CharField(max_length=256, blank=True, null=True, verbose_name=_("iconographia.object.color"))
    ovrigt = models.TextField(blank=True, null=True, verbose_name=_("iconographia.object.miscellaneous"))
    sokord = models.CharField(max_length=512, blank=True, null=True, verbose_name=_("iconographia.object.query"))
    motiv = models.TextField(blank=True, null=True, verbose_name=_("iconographia.object.motif"))
    litteratur = models.TextField(blank=True, null=True, verbose_name=_("iconographia.object.literature"))
    status = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.status"))
    titel = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.object.title"))
    parish = models.ForeignKey('Parish', models.DO_NOTHING, blank=True, null=True, verbose_name=_("iconographia.object.parish"))
    place = models.ForeignKey('Place', models.DO_NOTHING, blank=True, null=True, verbose_name=_("iconographia.object.place"))

    class Meta:
        managed = False
        db_table = 'object'
        verbose_name = _('iconographia.object.meta.singular_name')
        verbose_name_plural = _('iconographia.object.meta.plural_name')

    def __str__(self) -> str:
        return f"{self.objekt}, {self.cdh_category}"


class Parish(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("iconographia.parish.name"))
    variants = models.CharField(max_length=256, blank=True, null=True, verbose_name=_("iconographia.parish.variants"))
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("iconographia.parish.province"))
    diocese = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("iconographia.parish.diocese"))
    diocese_med = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("iconographia.parish.diocese_med"))
    county = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("iconographia.parish.county"))
    # origin = models.ManyToManyField('self', related_name='id')
    # parent = models.ManyToManyField('self', related_name='id')
    origin = models.ForeignKey('iconographia.Parish', models.DO_NOTHING, blank=True, null=True, verbose_name=_("iconographia.parish.origin"))
    parent = models.ForeignKey('iconographia.Parish', models.DO_NOTHING, blank=True, null=True, related_name='parish_id', verbose_name=_("iconographia.parish.parent"))
    notbefore = models.CharField(max_length=16, blank=True, null=True, verbose_name=_("iconographia.parish.not_before"))
    notafter = models.CharField(max_length=16, blank=True, null=True, verbose_name=_("iconographia.parish.not_after"))
    note_year = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("iconographia.parish.note_year"))
    snid_4 = models.PositiveIntegerField(blank=True, null=True, verbose_name=_("iconographia.parish.snid_4"))
    wikidata = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("iconographia.parish.wikidata"))
    notes = models.TextField(blank=True, null=True, verbose_name=_("iconographia.parish.notes"))

    class Meta:
        managed = False
        db_table = 'parish'
        verbose_name = _('iconographia.parish.meta.singular_name')
        verbose_name_plural = _('iconographia.parish.meta.plural_name')

    def __str__(self) -> str:
        return f"{self.name}, {self.diocese}"


class Place(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("iconographia.place.name"))
    type = models.PositiveIntegerField(verbose_name=_("iconographia.place.type"))
    certainty_type = models.CharField(max_length=9, verbose_name=_("iconographia.place.certainty_type"))
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, verbose_name=_("iconographia.place.parent"))
    parish = models.ForeignKey(Parish, models.DO_NOTHING, blank=True, null=True, verbose_name=_("iconographia.place.parish"))
    certainty = models.CharField(max_length=9, verbose_name=_("iconographia.place.certainty"))
    date_bebr = models.CharField(max_length=64, verbose_name=_("iconographia.place.date_bebr"))
    notbefore = models.CharField(max_length=32, verbose_name=_("iconographia.place.not_before"))
    notafter = models.CharField(max_length=32, verbose_name=_("iconographia.place.not_after"))
    type_indication = models.CharField(max_length=8, verbose_name=_("iconographia.place.type_indication"))
    note_year = models.CharField(max_length=128, verbose_name=_("iconographia.place.note_year"))
    wikidata = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("iconographia.place.wikidata"))
    geom = models.GeometryField(verbose_name=_("iconographia.place.geom"))
    municipality = models.CharField(max_length=256, blank=True, null=True, verbose_name=_("iconographia.place.municipality"))
    county = models.CharField(max_length=256, blank=True, null=True, verbose_name=_("iconographia.place.county"))
    country = models.CharField(max_length=32, blank=True, null=True, verbose_name=_("iconographia.place.country"))
    notes = models.TextField(blank=True, null=True, verbose_name=_("iconographia.place.notes"))
    exclude = models.CharField(max_length=3, blank=True, null=True, verbose_name=_("iconographia.place.exclude"))

    class Meta:
        managed = False
        db_table = 'place'
        verbose_name = _('iconographia.place.meta.singular_name')
        verbose_name_plural = _('iconographia.place.meta.plural_name')

    def __str__(self) -> str:
        return f"{self.name} in {self.county}, {self.country}"

