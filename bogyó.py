osember = input('Mi a neved?')
bogyo = int(input('Mennyi bogyót szedtél?'))
if bogyo < 10:
    print(osember, 'ügyetlen, mert', bogyo, 'bogyót szedett.')
elif 20 > bogyo >= 10:
    print(osember, 'ügyes, mert', bogyo, 'bogyót szedett.')
elif bogyo >= 20:
    print(osember, 'profi, mert', bogyo, 'bogyót szedett.')