from django.contrib import admin
from server.models import Channel, Video, VideoSponsor, Sponsor, SponsorDomain

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
  pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
  pass

@admin.register(VideoSponsor)
class VideoSponsorAdmin(admin.ModelAdmin):
  pass

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
  list_display = ['name', 'has_image']
  readonly_fields = ['has_image']
  def has_image(self, obj):
    return bool(obj.image)
  has_image.boolean = True

@admin.register(SponsorDomain)
class SponsorDomainAdmin(admin.ModelAdmin):
  list_display = ['domain', 'sponsor', 'no_promo', 'first_url']
  list_editable = ['no_promo', 'sponsor']
  list_filter = ['no_promo']
  readonly_fields = ['first_url']
  def first_url(self, obj):
    if obj.urls:
      return obj.urls[0]

