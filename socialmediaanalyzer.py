def analyze_post(post_text, likes, comments, shares, post_time, followers=1000):
    
    #  Analyze Post Content :
    
    # Count words 
    words = post_text.split()
    word_count = len(words)
    
    # Count hashtags (words starting with #)
    hashtag_count = sum(1 for word in words if word.startswith('#'))
    
    # Count mentions (words starting with @)
    mention_count = sum(1 for word in words if word.startswith('@'))
    
    
    # STEP 2: Calculate Engagement Rate
    engagement_score = likes + (comments * 2) + (shares * 3)
    engagement_rate = (engagement_score / followers) * 100
    
    
    # STEP 3: Determine Best Posting Time
    if 6 <= post_time < 9:
        time_category = "early morning"
        tip = "Decent time - people check phones after waking up"
    elif 9 <= post_time < 12:
        time_category = "morning peak"
        tip = "Great time - coffee break scrolling!"
    elif 12 <= post_time < 17:
        time_category = "afternoon"
        tip = "Good time - lunch and work breaks"
    elif 17 <= post_time < 21:
        time_category = "evening peak"
        tip = "Excellent time - people are free after work/school"
    elif 21 <= post_time < 24:
        time_category = "night"
        tip = "Good time - before bed scrolling"
    else:  # 0 <= post_time < 6
        time_category = "late night"
        tip = "Low engagement - most people are sleeping"
    
    
    # STEP 4: Create Insights Dictionary
    insights = {
        'content_analysis': {
            'word_count': word_count,
            'hashtags': hashtag_count,
            'mentions': mention_count
        },
        'engagement_metrics': {
            'total_likes': likes,
            'total_comments': comments,
            'total_shares': shares,
            'engagement_score': engagement_score,
            'engagement_rate': round(engagement_rate, 2)
        },
        'posting_time': {
            'hour': post_time,
            'category': time_category,
            'recommendation': tip
        }
    }
    
    return insights


# EXAMPLE USAGE
print("=" * 60)
print("SOCIAL MEDIA POST ANALYSIS")
print("=" * 60)

#  Post 1: Morning post with good engagement
post1 = "Just launched my new art project! 🎨 Check it out! #art #creative #newproject Thanks @artgallery @friends"
likes1 = 150
comments1 = 45
shares1 = 30
time1 = 10  # 10 AM

print("\n📱 POST 1:")
print(f"Text: {post1}")
print(f"Posted at: {time1}:00 (10 AM)")
print(f"Stats: {likes1} likes, {comments1} comments, {shares1} shares")

result1 = analyze_post(post1, likes1, comments1, shares1, time1)

print("\n📊 ANALYSIS RESULTS:")
print(f"\n✍️ Content Analysis:")
print(f"   - Words: {result1['content_analysis']['word_count']}")
print(f"   - Hashtags: {result1['content_analysis']['hashtags']}")
print(f"   - Mentions: {result1['content_analysis']['mentions']}")

print(f"\n💡 Engagement Metrics:")
print(f"   - Engagement Score: {result1['engagement_metrics']['engagement_score']} points")
print(f"   - Engagement Rate: {result1['engagement_metrics']['engagement_rate']}%")

print(f"\n⏰ Posting Time:")
print(f"   - Category: {result1['posting_time']['category']}")
print(f"   - Tip: {result1['posting_time']['recommendation']}")


# Example Post 2: Evening post with moderate engagement
print("\n" + "=" * 60)

post2 = "Movie night with @bestfriend! 🍿 #movienight #weekend #fun"
likes2 = 85
comments2 = 20
shares2 = 10
time2 = 19  # 7 PM

print("\n📱 POST 2:")
print(f"Text: {post2}")
print(f"Posted at: {time2}:00 (7 PM)")
print(f"Stats: {likes2} likes, {comments2} comments, {shares2} shares")

result2 = analyze_post(post2, likes2, comments2, shares2, time2)

print("\n📊 ANALYSIS RESULTS:")
print(f"\n✍️ Content Analysis:")
print(f"   - Words: {result2['content_analysis']['word_count']}")
print(f"   - Hashtags: {result2['content_analysis']['hashtags']}")
print(f"   - Mentions: {result2['content_analysis']['mentions']}")

print(f"\n💡 Engagement Metrics:")
print(f"   - Engagement Score: {result2['engagement_metrics']['engagement_score']} points")
print(f"   - Engagement Rate: {result2['engagement_metrics']['engagement_rate']}%")

print(f"\n⏰ Posting Time:")
print(f"   - Category: {result2['posting_time']['category']}")
print(f"   - Tip: {result2['posting_time']['recommendation']}")


# Comparison
print("\n" + "=" * 60)
print("📈 COMPARISON:")
print("=" * 60)
print(f"Post 1 engagement rate: {result1['engagement_metrics']['engagement_rate']}%")
print(f"Post 2 engagement rate: {result2['engagement_metrics']['engagement_rate']}%")

if result1['engagement_metrics']['engagement_rate'] > result2['engagement_metrics']['engagement_rate']:
    print("✨ Post 1 performed better!")
else:
    print("✨ Post 2 performed better!")