# MovieRecomment

### Hướng dẫn cài đặt csdl neo4j: https://docs.google.com/document/d/1OHoGBVPPaAScQ5hjzqJ4Uryjng3DOzCviVUWAJM_M9w/edit?usp=sharing

## Cách chạy ứng dụng web

Install flask: 
```
pip install flask
```
https://code.tutsplus.com/vi/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

Vào thư mục project có file app.py và gõ lệnh python app.py để start web (lưu ý phải start neo4j)

![image](https://user-images.githubusercontent.com/75305838/208230080-a7d80e7e-f722-4f5f-b2df-a023eaadc93d.png)

Nếu không chạy được thì thay đổi driver username pass của DB

Các câu query truy vấn dữ liệu trong query.py (nếu muốn chạy neo4j thì đổi $param thành dữ liệu tương ứng)

```Python
# 10 bộ phim có doanh thu cao nhất
allMovie = '''
MATCH (n:Movie) RETURN n ORDER BY -n.revenue  LIMIT 8
'''

# Thông tin chi tiết của bộ phim
movieDetail = '''
MATCH (d:Director)-[:DIRECTED]->(n:Movie)<-[:ACTED_IN]-(a:Actor) WHERE n.movieId=$param  RETURN n,a, d 
'''

# Thông tin diễn viên đóng phim
actorOfMoive = '''
MATCH (n:Movie)<-[:ACTED_IN]->(a:Actor) RETURN n, a LIMIT 25
'''

# top 10 diễn viên có doanh thu phim lớn nhất
topActor = '''
MATCH (a:Actor)-[:ACTED_IN]->(m:Movie) WITH a as actor, SUM(m.revenue) as revenue ORDER BY -revenue  RETURN actor, revenue  LIMIT 10
'''

# Top phim theo thể loại trong 10 thập kỉ 
topGenre = '''
MATCH (m:Movie)-[:IN_GENRE]->(g:Genre) WHERE g.name=$param AND m.year >= 2012 AND m.year <= 2022 AND m.imdbRating IS NOT NULL RETURN m, g ORDER BY -m.revenue  LIMIT 10
'''

recommentMoive = '''
MATCH (m:Movie)<-[:RATED]-(u:User)-[:RATED]->(n:Movie) WHERE m.movieId =$param WITH n as movie, COUNT(u) AS people_rate ORDER BY people_rate DESC LIMIT 12 RETURN movie, people_rate 
'''

```





