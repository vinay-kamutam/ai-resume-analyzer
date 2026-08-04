function ProgressBar({ value, color = "bg-blue-600" }) {

    return (

        <div className="w-full bg-gray-200 rounded-full h-4 mt-3">

            <div
                className={`${color} h-4 rounded-full transition-all duration-700`}
                style={{ width: `${value}%` }}
            ></div>

        </div>

    );

}

export default ProgressBar;