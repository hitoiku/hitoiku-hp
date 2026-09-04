from icons import icon
from content_story import INTRO_HTML

STATIC_HERO = f"""
{INTRO_HTML}
<section class="static-hero">
  <div class="static-hero-media">
    <img src="images/hero.jpg" alt="人の可能性が、動き出す瞬間を。"
         width="1536" height="1024">
  </div>
  <div class="static-hero-text">
    <h1>人の可能性が、動き出す瞬間を。</h1>
    <p>採用して終わりではない。人が定着し、成長し、活躍するところまで。<br>ヒトイクは、採用から定着・活躍までを支援する採用コンサルティング会社です。</p>
  </div>
</section>
"""

CONTENT = f"""
{STATIC_HERO}

<section id="after-story">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">About Hitoiku</span>
      <h2>私たちについて</h2>
      <p>ヒトイクは、採用・研修・人事制度という「人」に関わる領域を横断しながら、人と組織の可能性を育てる会社です。</p>
      <p style="margin-top:20px;"><a href="about.html" class="more" style="color:var(--brand);font-weight:700;display:inline-flex;align-items:center;gap:6px;">私たちについてを詳しく見る {icon('arrow-right')}</a></p>
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Our Services</span>
      <h2>何を支援しているか</h2>
      <p>採用・育成・制度はそれぞれ独立したものではなく、つながって初めて機能します。</p>
    </div>
    <div class="service-grid">
      <div class="service-card reveal">
        <div class="service-card-photo">
          <img src="images/service-recruiting.jpg" alt="採用コンサルティング" loading="lazy">
          <div class="icon">{icon('target')}</div>
        </div>
        <div class="service-card-body">
        <div class="tag">01 / RECRUITING</div>
        <h3>採用コンサルティング</h3>
        <p>採用代行ではなく"採用の仕組み"をつくる。戦略設計から実務、面接官育成、定着支援までを一気通貫でサポートします。</p>
        <ul><li>採用戦略・要件設計</li><li>母集団形成・実務支援</li><li>面接官研修・定着支援</li></ul>
        <a href="recruiting.html" class="more">詳しく見る {icon('arrow-right')}</a>
        </div>
      </div>
      <div class="service-card reveal">
        <div class="service-card-photo">
          <img src="images/service-training.jpg" alt="研修・人材育成" loading="lazy">
          <div class="icon">{icon('brain')}</div>
        </div>
        <div class="service-card-body">
        <div class="tag">02 / TRAINING</div>
        <h3>研修・人材育成</h3>
        <p>心理学×体験学習で、行動変容を生み出す研修。「受けて終わり」にしない、現場で機能する育成をつくります。</p>
        <ul><li>管理職研修・評価者研修</li><li>面接官研修</li><li>リーダーシップ／ロジカルシンキング</li></ul>
        <a href="training.html" class="more">詳しく見る {icon('arrow-right')}</a>
        </div>
      </div>
      <div class="service-card reveal">
        <div class="service-card-photo">
          <img src="images/service-hrsystem.jpg" alt="人事制度・組織開発" loading="lazy">
          <div class="icon">{icon('layers')}</div>
        </div>
        <div class="service-card-body">
        <div class="tag">03 / HR SYSTEM</div>
        <h3>人事制度・組織開発</h3>
        <p>採用した人が育ち、評価され、活躍し続けるための土台づくり。等級・評価・処遇制度を、現場で機能する形で設計します。</p>
        <ul><li>等級・評価・処遇制度設計</li><li>評価者研修</li><li>制度運用支援</li></ul>
        <a href="hr-system.html" class="more">詳しく見る {icon('arrow-right')}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center reveal" style="margin-left:auto;margin-right:auto;">
      <span class="eyebrow">Client Voice</span>
      <h2>導入企業様の声</h2>
    </div>
    <div class="stat-showcase reveal">
      <div class="stat-showcase-item">
        <div class="stat-ring-wrap">
          <svg class="stat-ring" viewBox="0 0 120 120"><circle cx="60" cy="60" r="52" class="stat-ring-track"/><circle cx="60" cy="60" r="52" class="stat-ring-bar" style="--pct:98;"/></svg>
          <div class="stat-showcase-num">98<span>%</span></div>
        </div>
        <div class="stat-showcase-label">研修内容の満足度</div>
      </div>
      <div class="stat-showcase-item">
        <div class="stat-ring-wrap">
          <svg class="stat-ring" viewBox="0 0 120 120"><circle cx="60" cy="60" r="52" class="stat-ring-track"/><circle cx="60" cy="60" r="52" class="stat-ring-bar" style="--pct:99;"/></svg>
          <div class="stat-showcase-num">99<span>%</span></div>
        </div>
        <div class="stat-showcase-label">講師対応の満足度</div>
      </div>
      <div class="stat-showcase-item">
        <div class="stat-ring-wrap">
          <svg class="stat-ring" viewBox="0 0 120 120"><circle cx="60" cy="60" r="52" class="stat-ring-track"/><circle cx="60" cy="60" r="52" class="stat-ring-bar" style="--pct:98;"/></svg>
          <div class="stat-showcase-num">98<span>%</span></div>
        </div>
        <div class="stat-showcase-label">リピート率</div>
      </div>
    </div>
    <div class="case-grid mt-lg">
      <div class="case-card reveal">
        <img class="case-photo" src="images/case-nursing.jpg" alt="株式会社ナーシング様 研修風景" loading="lazy">
        <div class="case-body">
          <span class="badge">研修導入事例</span>
          <h3>見えない課題を教えてくれる唯一のフィードバック</h3>
          <p>社内だけでは気づけない課題や本音の声を初めて知ることができ、業務の質が上がったことを実感。</p>
          <div class="org">株式会社ナーシング 様</div>
        </div>
      </div>
      <div class="case-card reveal">
        <img class="case-photo" src="images/case-karitsu.jpg" alt="カリツー株式会社様 研修風景" loading="lazy">
        <div class="case-body">
          <span class="badge">研修導入事例</span>
          <h3>心理学のエッセンスで、自分・メンバーと真剣に向き合えた</h3>
          <p>自分自身の考え方や在り方を見つめ直し、チームメンバーへの接し方にも変化が生まれた。</p>
          <div class="org">カリツー株式会社 様</div>
        </div>
      </div>
    </div>
    <p class="text-center mt-lg"><a href="works.html" class="btn btn-outline">支援実績をもっと見る {icon('arrow-right')}</a></p>
  </div>
</section>
"""
