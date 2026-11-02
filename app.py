import time
import streamlit as st

# 모바일 화면 최적화 설정
st.set_page_config(
    page_title="우리 몸 항산화 건강 도우미", page_icon="🧪", layout="centered"
)

COEF_PH = 8.3333
COEF_VITA = 33.3333
INTERCEPT = -15.0

SYMPTOM_MAPPING = {
    "1. 밥 먹고 속이 자주 쓰림 (위산 과다)": 2.0,
    "2. 피부가 건조하고 자주 가려움 (약산성)": 4.0,
    "3. 평소 몸 상태가 편안하고 보통임 (보통)": 7.4,
    "4. 속이 더부룩하고 가스가 참 (장내 염기성)": 8.0,
}

# 1단계: 2초 스플래시 로딩 연출
if "loaded" not in st.session_state:
    st.title("🧪 우리 몸 항산화 건강 도우미")
    st.subheader("우리 몸 항산화 반응을 분석하고 있습니다...")
    st.caption("체내 산도 환경과 비타민 C 반응 모델을 불러오는 중입니다")

    p_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)  # 2초 로딩
        p_bar.progress(i + 1)

    st.session_state["loaded"] = True
    st.rerun()

# 2단계: 순우리말 고르는 화면
st.title("🧪 우리 몸 항산화 건강 도우미")
st.info("📋 평소 몸 상태와 비타민 섭취 횟수를 선택해 주세요.")

symptom = st.selectbox("현재 몸 상태:", list(SYMPTOM_MAPPING.keys()))
vita = st.number_input(
    "비타민 C 섭취 횟수 (회):", min_value=0.0, max_value=10.0, value=1.0, step=0.5
)

# 3단계: 2초 게이지 상승 후 3선 보건 대책 팝업
if st.button("▶ 선택 완료 및 항산화 진단 시작 ◀", type="primary"):
    st.write("⏳ **2초간 체내 항산화 반응 게이지를 측정하고 있습니다...**")
    g_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        g_bar.progress(i + 1)

    ph_val = SYMPTOM_MAPPING[symptom]
    pred = (COEF_PH * ph_val) + (COEF_VITA * vita) + INTERCEPT
    result = min(100.0, max(0.0, pred))

    st.markdown("---")
    st.header(f"📊 예측 항산화율: **{result:.1f} %**")

    if result >= 90:
        st.success("🟢 **[분류 1] 매우 좋음** - 체내 항산화 반응이 완벽합니다.")
    elif result >= 60:
        st.warning("🟡 **[분류 2] 보통** - 항산화 반응이 적절한 수준입니다.")
    else:
        st.error(
            "🔴 **[분류 3] 위험** - 체내 산화 스트레스 예방 대책이 필요합니다."
        )

        with st.expander(
            "🚨 보건 지원 정책 3선 (산화 스트레스 취약계층 대책)", expanded=True
        ):
            st.markdown("""
            **1️⃣ 위장 산도 맞춤형 영양 바우처 지원**  
            - 위산 과다 및 소화기 질환 취약계층 대상 맞춤 비타민 C 무료 지원  
            
            **2️⃣ 청소년·고령층 산화 스트레스 정기 검진제**  
            - 지역 보건소 연계 체내 환경 측정 및 산화 수치 무료 정기 검진  
            
            **3️⃣ 학교·복지관 맞춤 영양 식단 보급**  
            - 개인별 몸 상태에 맞춘 맞춤 과일/채소 식단 정보 제공
            """)
