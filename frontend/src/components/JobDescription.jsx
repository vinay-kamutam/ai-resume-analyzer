function JobDescription({ jobDescription, setJobDescription }) {

    return (

        <div className="bg-white rounded-xl shadow-lg p-6 mt-6">

            <h2 className="text-xl font-bold mb-4">
                💼 Job Description
            </h2>

            <textarea
                className="w-full h-48 border rounded-lg p-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Paste the Job Description here..."
                value={jobDescription}
                onChange={(e) => setJobDescription(e.target.value)}
            />

        </div>

    );

}

export default JobDescription;