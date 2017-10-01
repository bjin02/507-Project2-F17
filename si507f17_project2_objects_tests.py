import unittest
from si507f17_project2_objects_code import *

##########
print("BELOW IS TEST OUTPUT FOR PROJECT 2 SI 507 F17 *****\n\n")


class Problem1(unittest.TestCase):
	def setUp(self):
		search_data1 = sample_get_cache_itunes_data("the beatles")["results"]
		songdata1 = search_data1[0]
		songdata2 = search_data1[1]
		search_data2 = sample_get_cache_itunes_data("ratatouille")["results"]
		self.m1inst = Media(search_data1[0])
		self.m2inst = Media(search_data2[0])

	def test_constructor_media(self):
		self.assertEqual(type(self.m1inst.title),type(u"s"),"Testing whether inst var is a unicode string (all web data is unicode, generally)")
		self.assertEqual(type(self.m1inst.author),type(u"s"),"Testing whether inst var is a unicode string (all web data is unicode, generally)")
		self.assertEqual(type(self.m1inst.itunes_URL),type(u"s"),"Testing whether inst var is a unicode string (all web data is unicode, generally)")
		self.assertEqual(type(self.m2inst.itunes_id),type(34))
		self.assertEqual(self.m2inst.title,"Ratatouille")
		self.assertTrue(self.m1inst.itunes_URL.startswith("http"))
		self.assertEqual(self.m2inst.itunes_id,265250067)

	def test_repr_method(self):
		self.assertEqual(self.m2inst.__repr__(),"ITUNES MEDIA: 265250067")

	def test_str_method(self):
		self.assertEqual(self.m1inst.__str__(), "Here Comes the Sun by The Beatles")

	def test_repr_method(self):
		self.assertEqual(self.m2inst.__repr__(),"ITUNES MEDIA: 265250067")

	def test_contains_method(self):
		self.assertTrue("beatles" not in self.m1inst)
		self.assertTrue("ouille" in self.m2inst)

	def tearDown(self):
		pass

class Problem2Song(unittest.TestCase):
	def setUp(self):
		search_data1 = sample_get_cache_itunes_data("the beatles")["results"]
		songdata1 = search_data1[0]
		songdata2 = search_data1[1]
		self.song1 = Song(songdata1)
		self.song2 = Song(songdata2)

	def test_song_constructor_override(self):
		self.assertEqual(type(self.song1.album),type(u""))
		self.assertEqual(type(self.song1.track_number),type(3))
		self.assertEqual(type(self.song1.genre),type(u""))
		self.assertEqual(self.song1.album,u"Abbey Road")
		self.assertEqual(self.song1.title,u"Here Comes the Sun")
		self.assertEqual(self.song1.genre,u"Rock")
		self.assertEqual(self.song1.track_number,7)
		self.assertTrue(self.song1.itunes_URL.startswith("http"))
		self.assertEqual(self.song1.itunes_id,401187150)

	def test_song_len(self):
		self.assertEqual(len(self.song1),185)

	def test_song_contains(self):
		self.assertTrue("Sun" in self.song1)
		self.assertTrue("Beat"not in self.song1)

	def tearDown(self):
		pass

class Problem2Movie(unittest.TestCase):
	def setUp(self):
		search_data2 = sample_get_cache_itunes_data("ratatouille")["results"]
		movie1 = search_data2[0]
		self.movie_sample = Movie(movie1)

	def test_movie_constructor_override(self):
		self.assertEqual(type(self.movie_sample.genre),type(u""))
		self.assertEqual(self.movie_sample.title,u"Ratatouille")
		self.assertEqual(self.movie_sample.genre,u"Kids & Family")
		self.assertEqual(self.movie_sample.rating,u"G")
		self.assertTrue(self.movie_sample.itunes_URL.startswith("http"))
		self.assertEqual(self.movie_sample.itunes_id,265250067)
		self.assertEqual(len(self.movie_sample.description),1342)

	def test_movie_len(self):
		self.assertEqual(len(self.movie_sample),111)

	def test_movie_str(self):
		self.assertEqual(self.movie_sample.__str__(),"Ratatouille by Pixar & Brad Lewis")

	def test_movie_repr(self):
		self.assertEqual(self.movie_sample.__repr__(),"ITUNES MEDIA: 265250067")

	def test_movie_contains(self):
		self.assertTrue("tatou" in self.movie_sample)
		self.assertTrue("Pixar" not in self.movie_sample)

	def tearDown(self):
		pass

class Problem3(unittest.TestCase):
	def setUp(self):
		search_data1 = sample_get_cache_itunes_data("the beatles")["results"]
		songdata1 = search_data1[0]
		self.song1 = Song(songdata1)
		search_data2 = sample_get_cache_itunes_data("ratatouille")["results"]
		movie1 = search_data2[0]
		self.movie_sample = Movie(movie1)
		self.media1 = Media(songdata1)


	def test_song_list(self):
		self.assertEqual(type(song_list[0]),type(self.song1))
		self.assertEqual(type(song_list[-1]),type(self.song1))
		self.assertTrue(len(song_list) == len(song_samples))

	def test_movie_list(self):
		self.assertEqual(type(movie_list[0]),type(self.movie_sample))
		self.assertEqual(type(movie_list[-1]),type(self.movie_sample))
		self.assertTrue(len(movie_list) == len(movie_samples))

	def test_media_list(self):
		self.assertEqual(type(media_list[0]),type(self.media1))
		self.assertEqual(type(media_list[-1]),type(self.media1))
		self.assertTrue(len(media_list) == len(media_samples))

	def tearDown(self):
		pass


if __name__ == '__main__':
	unittest.main(verbosity=2)


