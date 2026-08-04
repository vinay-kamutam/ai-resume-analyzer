import Card from "./Card";
import ProgressBar from "./ProgressBar";

function ATSScoreCard({ ats }) {

    if (!ats) return null;

    const score = ats.overall_score;

    let color = "bg-red-500";

    if (score >= 80)
        color = "bg-green-500";
    else if (score >= 60)
        color = "bg-yellow-500";

    return (

        <Card
            title="ATS Analysis"
            icon="🎯"
        >

            <div className="text-center mb-6">

                <h1 className="text-6xl font-bold text-blue-600">

                    {score}%

                </h1>

            </div>

            <ProgressBar
                value={score}
                color={color}
            />

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">

                <div>

                    <h3 className="font-bold text-green-600 mb-3">
                        ✅ Strengths
                    </h3>

                    <ul className="list-disc ml-5 space-y-2">

                        {ats.strengths?.map((item, index) => (

                            <li key={index}>{item}</li>

                        ))}

                    </ul>

                </div>

                <div>

                    <h3 className="font-bold text-red-600 mb-3">
                        ❌ Missing Skills
                    </h3>

                    <ul className="list-disc ml-5 space-y-2">

                        {ats.missing_skills?.map((item, index) => (

                            <li key={index}>{item}</li>

                        ))}

                    </ul>

                </div>

            </div>

            <div className="mt-8">

                <h3 className="font-bold text-orange-600 mb-3">
                    💡 Improvement Suggestions
                </h3>

                <ul className="list-disc ml-5 space-y-2">

                    {ats.improvement_suggestions?.map((item, index) => (

                        <li key={index}>{item}</li>

                    ))}

                </ul>

            </div>

            <div className="mt-8 p-5 bg-blue-50 rounded-xl">

                <h3 className="font-bold text-blue-700 mb-2">
                    ⭐ Hiring Recommendation
                </h3>

                <p>

                    {ats.hiring_recommendation}

                </p>

            </div>

        </Card>

    );

}

export default ATSScoreCard;